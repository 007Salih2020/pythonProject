# metaclass

# Type in python
num= 23
print("Type of num is:", type(num))

lst=[1,2,4]
print("Type of list is:", type(lst))

name = "Salih"
print("Type of name is:", type(name))


print(" - -  - - -  - -")

# every type defined by class

class Student:
    pass

stu_obj=Student()

# print type of object of Student Class
print("Type of stu_obj is: ", type(stu_obj))


print(" - -  - - -  - -")

# a class is also an object
class Student:
    pass


# print type of object of Student Class
print("Type of student class is: ", type(Student))

print("-  - - - - -  - -")
# define class without any class methods and variables

class test: pass

# defining method variables
test.x=45

# defining class methods
test.foo= lambda self: print("Hello")

# creating object
myobj = test()

print(myobj.x)
myobj.foo()

print(" - -  - - - - - - - ")
# Custom metaclass

## __new__() - it is method called before __init__(). it creates objects and returns it
## __init__() - this method just initialize the created object passed as a parameter

# example

def test_method(self):
    print("This is Test class method !")

# creating base class
class Base:
    def myfun(self):
        print("this is inherited method !")

# creating test class dynamically using type() method directly
Test = type('Test', (Base,), dict(x="Salih", my_method=test_method))

# print type of Test
print("Type of Test class:", type(Test))

# creating instance of Test class
test_obj = Test ()
print("Type of test_obj:", type(test_obj))

# calling inherited method
test_obj.myfun()

# calling Test class method
test_obj.my_method()

# printing variable
print(test_obj.x)

print("  - - - - - - - - - ")
# create metaclass without using type() directly
''' 
# our metaclass

class MultiBases(type):

    # overriding __new__ method
    def __new__(cls, clsname, bases, clsdict):

        # if no of base classes is greater than 1, raise error
        if len(bases)>1:
            raise TypeError("Inherited multiple base classes ! ! ! ")

        # else execute __new__ method super class, ie:  call __init__ of type class
        return super().__new__(cls,clsname,bases,clsdict)
# metacass can be specified by 'metaclass' keyword argument
# now multibase class is used for creating classes this would be propagated to all subclasses of Base

class Base(metaclass=MultiBases):
    pass

# no error is rased
class A(Base):
    pass

# no error is raised
class B(Base):
    pass

# this will raise an error !
class C(A,B):
    pass
'''
print(" - - - - - - - - - - - - ")
#
# solving problems with metaclas

from functools import wraps

def debug(func):
    ''' decorator for debugging passed function '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Full name of this method: ", func.__qualname__)
        return func(*args, **kwargs)
    return wrapper


def debugmethods(cls):
    ''' class decorator make us of debug decorator to debug class methods'''

    # check in class dictionary for any callable (method) if exist, replace it with debugged version
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls

# same class
@debugmethods
class Calc:
    def add(self, x,y):
        return x+y
    def mul(self,x,y):
        return x*y
    def div(self, x,y):
        return x/y

mycal = Calc()
print(mycal.add(2,3))
print(mycal.mul(5,2))

print(" - - - - - - - - - ")

# meta class based solution

from functools import wraps


def debug(func):
    '''decorator for debugging passed function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Full name of this method:", func.__qualname__)
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls):
    '''class decorator make use of debug decorator  to debug class methods '''

    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls


class debugMeta(type):
    '''meta class which feed created class object to debugmethod to get debug functionality enabled objects'''

    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        obj = debugmethods(obj)
        return obj


# base class with metaclass 'debugMeta' now all the subclass of this  will have debugging applied
class Base(metaclass=debugMeta): pass


# inheriting Base
class Calc(Base):
    def add(self, x, y):
        return x + y


# inheriting Calc
class Calc_adv(Calc):
    def mul(self, x, y):
        return x * y


# Now Calc_adv object showing debugging behaviour
mycal = Calc_adv()
print(mycal.mul(2, 3))


print(" - -  - - - - - - - - - - ")

#