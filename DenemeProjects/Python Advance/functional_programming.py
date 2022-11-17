# pure functions
# it always produces the same output for the same arguemnts
# it does not change or modifies the input variable

def pure_func(List):

    New_List= []

    for i in List:
        New_List.append(i**2)

    return New_List

# drivers code
Original_List =[1,2,3,4,5]
Modified_List= pure_func(Original_List)

print("Original List:", Original_List)
print("Modified List:", Modified_List)

print("- -  - - -  - ")
# Recursion

def Sum(L, i, n, count):

    # Base case
    if n<= i:
        return count

    count += L[i]

    # going into the recursion
    count = Sum(L, i+1, n, count)

    return count

# Drivers code
L = [1,2,3,4,5]
count = 0
n = len(L)
print(Sum(L, 0, n, count))


print("- -  - - -  - ")
# First Class and can be Higher-Order

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):

    # storing the function in a variable
    greeting = func("Hi, I am created by a function passed as an argument !")
    print(greeting)

greet(shout)
greet(whisper)

print("-  - - - -- - - ")
# Built-in Higher-order functions

# map()
## fun - it is a function that map passes each element of given iterable
## iter - it is a iterable which is to be mapped

# return double of n

def addition(n):
    return n + n

# we double all numbers using map()
numbers =(1,2,3,4,)
results = map(addition, numbers)

# does not print the value
print(results)

# for printing values
for result in results:
    print(result, end=" ")

print(" - - - - - ")
# filter()- filters the given sequence witht the help of a function that tests each element in the sequence to be true or not
# syntax: filter(function, sequence)

def fun(variable):

    letters = ['a', 'b','c','d','e']

    if (variable in letters):
        return True
    else:
        return False
# sequence
sequence = ['g','h','i','j','k','l','e']

# using filter function
filtered = filter(fun, sequence)

print("the filtered letters are:")

for s in filtered:
    print(s)


print(" - - - - - -")
# Lambda functions - create anonymous functions
## can have any number of arguments but only one expression
## one is free to use lambda functions wherever function objects are required
## syntactically restricted to a single expression
## various uses in particular fields of programming

cube = lambda x: x*x*x
print(cube(7))

L =[1,3,2,4,5,6]

is_even= [x for x in L if x % 2 == 0]

print(is_even)

print(" - - - - - - ")
# immutability

# string data types
immutable = "KurparkinWiesbaden"

# changing the values will raise an error
immutable[1] ='K'

print(" - - - - --- ")

#


