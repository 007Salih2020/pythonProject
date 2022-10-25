# defining decorator

def hello_decorator(func):

    def inner1():
        print("Hello, this is before function execution")

        # inside the wrapper function
        func()

        print("    This is after the function execution ")

    return inner1

# # defining function, to be called inside the wrapper
def function_to_be_used ():
    print("  This is inside the function ! !")

# passing function_to_be_used inside the decorator to control its behaviour

function_to_be_used = hello_decorator(function_to_be_used)

# now calling function
function_to_be_used()

# # #
# example -2

# importing libraries

import time
import math

# decorator to calculate the duration
def calculate_time(func):

    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()

        func (*args, **kwargs)

        # storing time after function execution
        end = time.time()

        print("total time takein in: ", func.__name__, end - begin)

    return inner1

# this can be added to any function present

@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes less time..
    time.sleep(2)
    print(math.factorial(num))

# calling the function
factorial(10)

##  # #

# what if a function returns sth or an argument is passed to the function

def hello_decorator(func):
    def inner1(*args, **kwargs):

        print("Before execution !")

        # getting returned value
        returned_value = func(*args, **kwargs)
        print("    After execution !!")

        # returning the value to the original frame
        return returned_value

    return inner1

# adding decorator
@hello_decorator
def sum_two_numbers(a, b):
    print("  Inside the Function")
    return a+b

a, b = 5, 10

# getting the value through return of the function
print("Sum=", sum_two_numbers(a,b))

#  # chaining decorators

def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor
def num():
    return 10

print(num())

 # ##



