# garbage collector   def __del__():

# simple example of destructors

class Employee:

    def __init__(self):
        # initializing
        print("Employee created .")

    # deleting (calling destructor)
    def __del__(self):
        print("Destructor called, Employee deleted")

obj= Employee()

del obj

# illustrate destructor -1

class Employee:

    def __init__(self):
        print("Employee created .")

    def __del__(self):
        print("Destructor called !")

def Create_obj():
    print("Making Object . .  .")
    obj = Employee()

    print("Function end . . . ")
    return obj

print("Calling Creae_obj() function . . .")
obj=Create_obj()
print("Program End")

# # illustrate destructor -2

class A:

    def __init__(self, bb):
        self.b = bb

class B:

    def __init__(self):
        self.a = A(self)

    def __del__(self):
        print("die")

def fun():
    b = B()

fun()

# #