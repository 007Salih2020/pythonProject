#

locals()['__builtins__']

# arithmetic error sample

try:
    a = 10/0
    print(a)

except ArithmeticError:
    print("This statement is raising an arithmetic exception")

else:
    print(" Success !")

print(" - -  - - -")

# key or index error sample

try:
    a=[1,2,3]
    print(a[3])

except LookupError:
    print("Index out of bound error !")

else:
    print("Success")

print(" -  - --  -")

# exception Attribute Error
''' 
class Attributes(object):
    pass

object = Attributes()
print(object.attribute)

'''
print("- - - - - -")

#  exception EOFError
''' 
while True:
    data = input('Enter Name:')
    print('Hello', data)
'''
print("- - - - - -")

# Floating Point Error
''' 
import math

print(math.exp(1000))

'''
print("- - - - - -")

#  exception GeneratorExit
''' 
def my_generator():
	try:
		for i in range(5):
			print ('Yielding', i)
			yield i
	except GeneratorExit:
		print ('Exiting early')

g = my_generator()
print (g.next())
g.close()
'''

print("- - - - - -")

# exception ImportError
''' 
import module_does_not_exit
'''
''' 
from exceptions import Userexception

'''

print("- - - - - -")

# exception ModuleNotFoundError
# exception IndexError
''' 
array = [0, 1, 2]
print(array[3])
'''

print("- - - - - -")

# exception KeyError
''' 
array ={'a':1, 'b':2}
print(array['c'])

'''


print("- - - - - -")

# exception Keyboard Interrupt

'''
try:
    print ('Press Return or Ctrl-C :',)
    ignored = input ()
except Exception, err:
    print('Caught exception:', err)
except KeyboardInterrupt, err:
    print('Caught KeyboardInterrupt')
else:
    print('No exception')
'''

print("- - - - - -")

# exception MemoryError

''' 
def fact(a):
    factors = []
    for i in range (1, a+1):
        if a % i == 0 :
            factors.append(i)
    return factors

num = 600851475143
print(fact(num))
'''

print("- - - - - -")

# exception NameError

''' 
def func():
    print ans
    
func()
'''

print("- - - - - -")

# exception NotImplementError

''' 
class BaseClass(object):
    """ Defines the interface """
    def __init__(self):
        super(BaseClass, self).__init__()
    def do_something(self):
        """ The Interface, not implement """
        raise NotImplementedError(self.__class__.__name__+'.do_something')

class SubClass(BaseClass):
    """ Implementss the interface """
    def do_something(self):
        """ really does something """
        print(self.__class__.__name__+'doing something')

SubClass().do_something()
BaseClass().do_something()
'''

print("- - - - - -")

# exception OSError([arg])
''' 
def func():
    print (ans)

func()
'''
print("- - - - - -")

# exception OverflowError
''' 
import sys
print('Regular Integer : (maxint=%)' % sys.maxint)

try:
    i = sys.maxint * 3
    print('No overflow for', type(i), 'i=', i)

except OverflowError, err:
    print('Overflowed at', i, err)

print()

print('Long Integer:')
for i in range(0, 100, 10):
    print('%2d' % i, 2L ** i)

print()
print('Floating point values:')

try:
    f = 2.0**i
    for i in range (100):
        print(i, f)
        f = f ** 2
except OverflowError, err:
    print('Overflowed after', f, err)
'''

print("- - - - - -")

# exception RecursionError
# exception ReferenceError

'''
import gc
import weakref

class Foo(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('(Deleting %s)' % self)
obj = Foo('obj')
p = weakref.proxy(obj)

print('BEFORE: ', p.name)
obj = None

print('AFTER:', p.name)

'''


print("- - - - - -")

# exception RuntimeError
# exception StopIteration

'''
Arr = [3, 1, 2]
i = iter(Arr)

print(i)
print(i.next())
print(i.next())
print(i.next())
print(i.next())

'''

print("- - - - - -")

# exception SyntaxError

'''
try:
    print(eval('I love Wiesbaden'))
except SyntaxError, err:
    print('Syntax error %s (%s-%s): %s' % \
          (err.filename, err.lineno, err.offset, err.text))
    print(err)

'''

print("- - - - - -")

# exception SystemError
# exception SystemExit
# exception TypeError

'''
arr = ('tuple',) + 'string'
print(arr)

'''

print("- - - - - -")

# exception UnboundLocalError

'''
def global_name_error():
    print(unknown_global_name)
    
def unbound_local():
    local_val = local_val + 1
    print(local_val)

try:
    global_name_error()
except NameError, err:
    print('Global name error:', err)
    
try:
    unbound_local()
except UnboundLocalError, err:
    print('Local name error:', err)
    
'''

print("- - - - - -")

# exception UnicodeError
# exception ValueError

'''
print(int('a'))
'''

print("- - - - - -")

# exception ZeroDivisionError

'''
print(1/0)
'''