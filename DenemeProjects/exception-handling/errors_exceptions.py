# syntax errors and logical errors

# syntax error sample
# initialize amount variable
amount = 10000

# check that you are eligible to purchase dsa self paced or not
''' 
if (amount > 2999)
    print("you are eligible to purchase Dsa Self Paced ")

'''
print( " - - - - ")

# logical errors sample

# initialize amount
marks = 1000
''' 
# perform division with 0
a = marks / 0
print(a)
'''
print("- -  - - - -")

# or indentation is not correct
''' 
if(a<3):
print("wiesbaden kurrr")
'''

print(" - - - -")
# put unsafe operation in try block

try:
    print("code start")
     # unsafe operation perform
    print(1/0)
# if error occur the it goes in except block
except:
    print("an error occurs")
# finally code in finally block
finally:
    print(" I love Wiesbaden ")

print("- - - - - - ")
# Raising exception for a predefined condition

try:
    amount=1999
    if amount < 2999:
        # raise the ValueError
        raise ValueError("Please add money in your account !")
    else:
        print("You are eligible to purchase DSA Self Paced course")

# if false then raise the value error
except ValueError as e:
    print(e)


