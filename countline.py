# countline.py
# counting lines of java file or java files in a dir

import os
import sys

def process_file(path):
    total = 0
    if (path.endswith('.java')):
        handle = open(path, 'r')
        for eachLine in handle:
            if len(eachLine) > 1:
                #print len(eachLine), ' > ', eachLine,
                eachLine = eachLine.lstrip()
                if (eachLine.startswith("//") == False):
                    total += 1
        handle.close()
        print path, ',', total, 'lines.'
    return total

def process_dir(path):
    total = 0
    listfile = os.listdir(path)
    for filename in listfile:
        filepath = path + '/' + filename
        if(os.path.isdir(filepath)):
            # exclude hidden dirs
            if(filename[0] == '.'):
                pass
            else:
                total += process_dir(filepath)
        elif(os.path.isfile(filepath)):
            total += process_file(filepath)
    return total

def process(path):
    total = 0
    if(os.path.isdir(path)):
        total = process_dir(path)
    elif(os.path.isfile(path)):
        total = process_file(path)

    print '>>> total lines :', total, '.'
    return total

#process('/home/kesalin/test/test/AccountPreference.java')
process('/home/kesalin/test/Settings')
