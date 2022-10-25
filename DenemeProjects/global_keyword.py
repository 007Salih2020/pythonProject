# accessing global variable inside a function

#global variable
a=15
b=10

#function to perform addddition

def add():
    c=a+b
    print(c)

# calling  a function
add()

# assign new value


a=15

# change a global value
''' 
def change():
    b = a+5
    a = b
    print(a)

change()
'''
# changing global variable inside a function using global

x = 15

def change():
    # using global keyword
    global x

    # increment value of a by 5
    x = x + 5
    print("Value of x inside a function :", x)

change()
print("Value of x outside a function :", x)

# modifying list elements without using global keyword

arr=[10,20,30]

def fun():
    for i in range(len(arr)):
        arr[i] +=10

print(" 'arr' list before executing fun():", arr)
fun()
print(" 'arr' list after executing fun(): ", arr)

# nested functions

def add():
    x = 15
    def change():
        global x
        x = 20
    print("Before making changing:", x)
    print("Making change")
    change()
    print("After making change: ", x)

add()
print("value of x", x)

#

