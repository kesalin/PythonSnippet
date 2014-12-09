from types import IntType
import math

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
print '\n------------Operator----------------'
powerValue = 3 ** 2
print powerValue

value1 = 1 / 2
value2 = 1.0 / 2.0

# floor devision
value3 = 1 // 2
value4 = 1.0 // 2.0

print 'Value1: ', value1, ', Value2: ', value2
print 'Value3: ', value3, ', Value4: ', value4

# tuple & list
print '\n------------Tuple & List----------------'
aList = [1, 2, 3, 4, 5, 'A', 'B', 'C']
print aList

print aList[0]
print aList[:3]
print aList[3:]

print '4 is in list: ', (4 in aList)
print '0 is not in list: ', (0 not in aList)

aTuple = ('A string', 77, 80.0, 'Another string', 'A', 123)
print aTuple

print aTuple[0]
print aTuple[:3]
print aTuple[3:]

# dictionary
print '\n------------Dictionary----------------'
aDict = {'host' : 'kesalin.github.io'}
aDict['port'] = 80
print aDict

for key in aDict.keys():
    print key, ':', aDict[key]

# range
print '\n------------Range----------------'
print range(0, 10, 2)

for num in range(4):
    print num

abc = 'abc'
for ch in abc:
    print ch

for i, ch in enumerate(abc):
    print 'index', i, ':', ch

# list
print '\n------------List parse----------------'
squared = [x ** 2 for x in range(4)]
for i in squared:
    print i

# file
print '\n------------File----------------'
enablePrintFile = False
handle = open('Syntax.py', 'r') # r-read, w-write, a-append, +-read and write, b-binary
for eachLine in handle:
    if enablePrintFile:
        print eachLine,
handle.close()

# functions
print '\n------------Functions----------------'
a = 123
b = [1, 2, 3]
print 'type of a is ', type(a)
print 'type(1) is IntType: ', (type(1) is IntType)
print 'length of b is ', len(b)
print 'cmp(0xFF, 255): ', cmp(0xFF, 255)
print 'str(a): ', str(a)
print 'ord(\'a\'): ', ord('a') 
print 'chr(97): ', chr(97)
print 'abs(-10.0): ', abs(-10.0)
print 'build a tuple coerce(1j, 134L): ', coerce(1j, 134L)
print 'return divisor and remainder: ', divmod(10, 3)
print 'pow(2, 3, 3) is pow(2, 3) % 3 : ', pow(2, 3, 3)
print 'int(3.9): ', int(3.9)
print 'round(3.9): ', round(3.9)
print 'math.floor(3.9)', math.floor(3.9)
print 'hex(28): ', hex(28), ', oct(28): ', oct(28)

# class
print '\n------------Class----------------'

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
print 'foo isinstance FooClass: ', isinstance(foo, FooClass)

foo.showName()
foo.showVersion()
print foo.addMe2Me(10)
print foo.addMe2Me('abc')
