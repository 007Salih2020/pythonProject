# sample illustration

def divide(x, y):
    try:

        # floor division : gives only fractional part as answer
        result = x // y
        print("yeah ! your answer is :", result)

    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

# look at parameters and note the working of program
divide(3,2)
divide(3, 0)

print(" - - -  - - - ")

# Else clause

def AbyB(a, b):

   try:
        c =((a+b)//(a-b))
   except ZeroDivisionError:
        print("a/b result in 0")
   else:
        print(c)

# driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

print(" - - --  -- ")

# Finally Keyword in python

try:
    k = 5//0  # raises divide by zero exception

# handles zerodivision excepiton
except ZeroDivisionError:
    print("Cant divide by zero")

finally: # this block is always executed regardless of exception generation
    print("This is always executed !")


print(" - - -- - -")

#
