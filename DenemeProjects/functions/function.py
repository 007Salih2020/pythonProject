# function return type

def add(num1: int, num2:int) -> int:
    """ Add two numbers """
    num3 = num1 + num2
    return num3


num1, num2 = 5, 15
ans = add (num1, num2)
print(f"the addition of {num1} and {num2} results {ans}")

# some more functions

def is_prime(n):
    if n in [2,3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <=n :
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(78), is_prime(79))

# simple arguments
# wheter x is even or odd

def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
evenOdd(2)
evenOdd(3)

# demonstrate default arguments
'''
check_mk_logwatch_checks:
  - comment: RMS-32
    file: /opt/sonarqube/logs
    patterns:
      - "C TRACE"
'''

# demonstrate defaul argument

def myFun(x, y=50):
    print("x:", x)
    print("y: ",y)
myFun(10)

# demonstrate Keyword Arguments

def student(firstname, lastname):
    print(firstname, lastname)
student(firstname="salilh", lastname="ozkan")
student(lastname="Elma", firstname="Work")

# variable non-keyword arguments
def myFun(*argv):
    for arg in argv:
        print(argv)
myFun("Hello","Welcome", "to", "Home")
myFun('Hello','Welcome', 'to', 'Home')

# *kwargs for variable number of keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key,value))
myFun(first="how", mid="are", last="you")

# docstring

def evenOdd(x):
    ''' Function to check if the number is even or odd '''
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

print(evenOdd.__doc__)

# return statement

def square_value(num):
    ''' This funciton returns the square value of the entered number'''
    return  num**2

print(square_value.__doc__)
print(square_value(2))
print(square_value(-4))

# pass by reference or by value

def myFun(x):
    x[2] = 20

list= [10,11,12,13,14,15]
myFun(list)
print(list)

# pass
def myFun(x):
    x=[20,30,40]

list=[10,11,12,13,14,15]
myFun(list)
print(list)

# mix
def swap(x,y):
    temp=x
    x=y
    y=temp

x=2
y=3
swap(x,y)
print(x)
print(y)

#  anonymous functions

def cube(x): return x*x*x

cube_v2= lambda x : x*x*x

print(cube(7))
print(cube_v2(7))

# function within function
def f1():
    s= "I love Wiesbaden"
    def f2():
        print(s)
    f2()
f1()

#