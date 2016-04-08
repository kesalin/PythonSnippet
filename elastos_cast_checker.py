# elastos_cast_checker.py
# encoding: UTF-8
# usages:
#        sudo chmod a+x elastos_cast_checker.py
#        python elastos_cast_checker.py

import re
import os
import sys

def read_file(path):
    lines = []
    if (path.endswith('.cpp') or path.endswith('.h')):
        if(os.path.isfile(path)):
            handle = open(path, 'r')
            for line in handle:
                lines.append(line.strip())
            handle.close()
    return lines

def find_declare_match(param, line):
    pattern = re.compile(r'AutoPtr\s*<(.*)>\s*(.*)'+'[, ]'+param+'[; ,]')
    return pattern.search(line)


def check_declare_match(usedType, param, declLine):
    pattern = re.compile(r'AutoPtr\s*<\s*'+usedType+'\s*>\s*(.*)'+'[, ]'+param+'[; ,]')
    return pattern.search(declLine)


def find_declare_line(param, lines, lineIndex):
    if len(lines) == 0:
        return -1

    for i in range(lineIndex, 0, -1):
        line = lines[i]
        if (len(line) > 1) and (line.startswith("//") == False):
            match = find_declare_match(param, line)
            if match:
                #print line, 'match', match.group()
                return i;
    return -1


def check_match(firstLog, logFile, cppFilepath, usedMatch, usedLineNum, declLine, declLineNum, isHeader = True):
    usedType = usedMatch.group(2)
    param = usedMatch.group(4)
    matchInfo = usedMatch.group()

    match = check_declare_match(usedType, param, declLine)
    if match == None:
        if firstLog:
            firstLog = False
            logInfo ='\n>> process file: ' + cppFilepath + '\n'
            logFile.write(logInfo)
            print logInfo

        fileInfo = ''
        if isHeader:
            fileInfo = 'in .h file'
        logInfo = "   > error: invalid using of {0} at line {1:d}, it is declared as {2} '{3}' at line {4:d}.\n" \
            .format(matchInfo, usedLineNum + 1, declLine, fileInfo, declLineNum + 1)
        logFile.write(logInfo)
        print logInfo
    else:
        #print 'match ', matchInfo, declLine
        return firstLog


def process_declare_line_in_header(logFile, firstLog, cppFilepath, match, lines, lineNum, headerFilepath):
    headerLines = read_file(headerFilepath)
    param = match.group(4)
    matchInfo = match.group()

    declLineNum = find_declare_line(param, headerLines, len(headerLines)-1)
    if (declLineNum != -1):
        declLine = headerLines[declLineNum]
        #print 'declLine', declLine
        firstLog = check_match(firstLog, logFile, cppFilepath, match, lineNum, declLine, declLineNum)
    else:
        logInfo = ''
        if firstLog:
            firstLog = False
            logInfo ='\n>> process file: ' + cppFilepath + '\n'
            logFile.write(logInfo)
            print logInfo

        if param.startswith('m'):
            logInfo = "   = warning: declaration for {0} at line {1:d} not found! is it declared in super class's .h file?\n".format(matchInfo, lineNum + 1)
        else:
            logInfo = "   = warning: declaration for {0} at line {1:d} not found!\n".format(matchInfo, lineNum + 1)
        logFile.write(logInfo)
        print logInfo
    return firstLog


def process_file(path, logFile):
    if path.endswith('.cpp') == False:
        return

    firstLog = True;
    lines = read_file(path)
    lineNum = 0
    for eachLine in lines:
        if (len(eachLine) > 1) and (eachLine.startswith("//") == False):
            pattern = re.compile(r'(\()(I\w*)(\*\*\)&)([a-zA-Z]\w*)(\))')
            match = pattern.search(eachLine)
            if match:
                #print match.group() match.groups()
                #print match.group(2), match.group(4)
                usedType = match.group(2)
                param = match.group(4)

                # do not check weak-reference Resolve
                if usedType == 'IInterface' and eachLine.find('->Resolve(') != -1:
                    pass
                else:
                    declLineNum = find_declare_line(param, lines, lineNum)
                    if (declLineNum != -1):
                        declLine = lines[declLineNum]
                        #print 'declLine', declLine
                        firstLog = check_match(firstLog, logFile, path, match, lineNum, declLine, declLineNum, False)
                    else:
                        headerFilepath = path.replace("/src/", "/inc/").replace(".cpp", ".h")
                        firstLog = process_declare_line_in_header(logFile, firstLog, path, match, lines, lineNum, headerFilepath)
        lineNum = lineNum +1


def process_dir(path, logFile):
    listfile = os.listdir(path)
    for filename in listfile:
        filepath = path + '/' + filename
        if(os.path.isdir(filepath)):
            # exclude hidden dirs
            if(filename[0] == '.'):
                pass
            else:
                process_dir(filepath, logFile)
        elif(os.path.isfile(filepath)):
            process_file(filepath, logFile)

def summarize_log(logPath):
    if(os.path.isfile(logPath)):
        errorCount = 0
        warningCount = 0

        # summarize
        logFile = open(logPath, 'r')
        for line in logFile:
            line = line.strip()
            if line.startswith('> error:') == True:
                errorCount = errorCount + 1
            elif line.startswith('= warning:') == True:
                warningCount = warningCount + 1
        logFile.close()

        # log
        logFile = open(logPath, 'a')
        logInfo = '\ntotal: {0:d} errors, {1:d} warnings.'.format(errorCount, warningCount)
        logFile.write(logInfo)
        print logInfo
        logFile.close()

def process(path, logPath):
    if(os.path.isfile(logPath)):
        os.remove(logPath)
    logFile = open(logPath, 'a')
    print 'output to', logPath
    if(os.path.isdir(path)):
        process_dir(path, logFile)
    elif(os.path.isfile(path)):
        process_file(path, logFile)
    else:
        print 'invalid path:', path
    logFile.close()
    summarize_log(logPath)

#process('/home/kesalin/test/python/test.cpp', 'elastos_cast_checker.log')

#total: 2 errors, 10 warnings.
#process('/home/kesalin/Elastos5/Sources/Elastos/LibCore/src', '/home/kesalin/elastos_cast_checker.log')

#process('/home/kesalin/Elastos5/Sources/Elastos/Frameworks/Droid/Base/Core/src/', '/home/kesalin/elastos_cast_checker.log')

#total: 7 errors, 0 warnings.
process('/home/kesalin/Elastos5/Sources/Elastos/Frameworks/Droid/Base/Services/Server/src', '/home/kesalin/elastos_cast_checker.log')
