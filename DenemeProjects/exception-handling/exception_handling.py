# there are two types of errors: syntax erors and Exceptions

# example for syntax error
'''
# initialize amount variable
amount = 1000

# chet that you are eligible to purchase DSA self paced or not

if(amount >2999)
print("you are eligible to purchase DSA Self Paced ")

# after the if condition, we get syntax error
'''
print("- - - - -")
# example for exception
''' 
# initialize the amount variable
marks = 10000
#perform division with 0
a = marks / 0
print(a)

# here raised ZeroDivisionError 
'''
print(" - - - - - ")

# Try and Except Statement

a = [1,2,3]
try:
    print("Second element = %d" %(a[1]))

    # Throws error since there are only 3 elements in array

    print("Fourth element = %d" %(a[3]))

except:
    print("An error occurred")

print(" - - - - - ")
# catching specific exception

def fun(a):
    if a < 4:

        # throw ZeroDevisionError for a = 3
        b = a/(a-3)

    #throws NameError if a >= 4
    print("Value of b=", b)

try:
    fun(3)
    fun(5)
# brackets are necessary here for multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

print("- - - - ")
# try with Else clause

def AbyB(a, b):
    try:
        c = ((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in =")
    else:
        print(c)

# Driver program to test above function
AbyB(2.0,3.0)
AbyB(3.0, 3.0)


print(" - - - -")
# finally keyword

try:
    k = 5//0  # raises divide by zero exception
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't dividie by zero")

finally:   # this block is always executed regardless of exception generation
    print("This is always executed")

print(" - - - -")

# raising exception

try:
    raise NameError ("Hi there")   # raise Error

except NameError:
    print("An Exception")
    raise  # To determine whether the exception was raised or not


print(" - - - - ")