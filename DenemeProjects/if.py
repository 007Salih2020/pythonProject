# python program to illustrate if statement
i=20

if (i<15):
    print("i is smaller than 15")
    print("I am   in if Block")
else:
    print("i is bigger than 15")
    print("I am   in Else Block")
print("I am NOT in if and Not in Else Block")

# ## #
# explicit function

def digitSum(n):
    dsum=0
    for ele in str(n):
        dsum+=int(ele)
    return dsum

# initializing list
List=[367, 111, 562, 945, 6726, 873]

# using function on odd elements of the list
newList=[digitSum(i) for i in List if i & 1]

print(newList)

#  #  #

# nested If statement

i=10
if(i == 10):

    if(i<15):
        print("i is smaller than 15")

    # nested if
    # will only be executed if the above statement is true

    if (i<12):
        print("i is smaller than 12")
    else:
        print("i is greater than 15")


# #  # #
i = 10

print(True) if i<15 else print(False)

