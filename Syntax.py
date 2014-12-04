import sys
import os

print 'Hello Python!'

# input/output
print '------------Input/Output----------------'
enableInputOutput = False
if enableInputOutput:
    user = raw_input('Enter your name:\n')
    print 'Your name is %s' % user

    ageStr = raw_input('Enter your age:\n')
    print 'Your age is %d' % int(ageStr)

# operator
print '------------Operator----------------'
powerValue = 3 ** 2
print powerValue

value1 = 26 / 3.0
value2 = 26 // 3.0
print 'Value1: %d, Value2: %d' % (value1, value2)

# tuple & list
print '------------Tuple & List----------------'
aList = [1, 2, 3, 4, 5, 'A', 'B', 'C']
print aList

print aList[0]
print aList[:3]
print aList[3:]

aTuple = ('A string', 77, 80.0, 'Another string', 'A', 123)
print aTuple

print aTuple[0]
print aTuple[:3]
print aTuple[3:]

# dictionary
print '------------Dictionary----------------'
aDict = {'host' : 'kesalin.github.io'}
aDict['port'] = 80
print aDict

for key in aDict.keys():
    print key, ':', aDict[key]

# range
print '------------Range----------------'
for num in range(4):
    print num

str = 'abc'
for ch in str:
    print ch

for i, ch in enumerate(str):
    print ch, '(%d)' % i

# list
print '------------List parse----------------'
squared = [x ** 2 for x in range(4)]
for i in squared:
    print i

# file
print '------------File----------------'
enablePrintFile = False
handle = open('Syntax.py', 'r') # r-read, w-write, a-append, +-read and write, b-binary
for eachLine in handle:
    if enablePrintFile:
        print eachLine,
handle.close()

# functions
print '------------Functions----------------'
a = 123
b = [1, 2, 3]
print 'type of a is %s' % type(a)
print 'length of b is %d' % len(b)


# class
print '------------Class----------------'

class FooClass:
    """my very first class: FooClass"""
    version = 0.1   # class (data) attribute.

    def __init__(self, nm='kesalin'):
        """constructor"""
        self.name = nm # class instance (data) attribute
        print 'Created a class instance for', nm

    def showName(self):
        """display instance attribute and class name"""
        print 'Your name is', self.name
        print 'My name is', self.__class__.__name__

    def showVersion(self):
        """display class attribute"""
        print self.version  # references FooClass.version

    def addMe2Me(self, x): # does not use 'self'
        """apply + operation to argument"""
        return x + x

foo = FooClass()
print type(foo)

foo.showName()
foo.showVersion()
print foo.addMe2Me(10)
print foo.addMe2Me('abc')
