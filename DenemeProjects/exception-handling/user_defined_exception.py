# sample

# class MyError is derived from super class exception
class MyError(Exception):

    # constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return (repr(self.value))

try:
    raise (MyError(3*5))

# value of exception is stored in error
except MyError as error:
    print('A New Exception occurred:', error.value)


print("- - - - - -")

# customizing Exception Classes

#  list all the exception

help(Exception)



print("- - - - - -")

#  User Defined class with Multiple Inheritance - example -1
# define Python user-defined exceptions
class Error(Exception):
    """ Base class for other exceptions """
    pass

class zerodivision(Error):
    """ Raise when the input value is zero """
    pass

try:
    i_num = int(input("Enter a number: "))
    if i_num == 0:
        raise zerodivision

except zerodivision:
    print("Input value is zero, try again !")
    print()




print("- - - - - -")

#  User Defined class with Multiple Inheritance - example -2
# Derivint Error from Super Class Exception

class Error(Exception):

    # error is derived class for exception but Base class for exceptions in this module
    pass

class TransitionError(Error):

    # raised when an operation attempts a state transition thats not allowed
    def __init__(self, perv, nex, msg):
        self.perv = perv
        self.nex = nex

        # error message thrown is saved in msg
        self.msg = msg

try:
    raise (TransitionError(2, 3*2, "Not Allowed"))
except TransitionError as error:
    print('Exception occurred:', error.msg)


print("- - - - - -")

# use standard Exception as a base class

# networkError has base RuntimeError and not exception

class Networkerror(RuntimeError):

    def __init__(self, arg):
        self.args = arg

try:
    raise Networkerror("Error")
except Networkerror as e:
    print(e.args)

