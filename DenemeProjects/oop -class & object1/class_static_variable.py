# static variable w

# class for computer science student
class CSStudent:
    stream = "cse"   #  class variable

    def __init__(self, name, roll):
        self.name = name    # instance variable
        self.roll = roll    # instance variable

# Objects of CSStudent class
a = CSStudent('Python', 1)
b = CSStudent('DevOps', 2)

print(a.stream)   # prints cse
print(b.stream)   # prints cse

print(a.name)     # prints Python
print(b.name)     # prints Devops

print(a.roll)     # prints 1
print(b.roll)     # prints 2


# class varibles can be accessed using class name also
print(CSStudent.stream)   # prints cse

# now if we change the stream for just a it wont be changed for b
a.stream = 'ece'
print(a.stream)    # prints ece
print(b.stream)    # prints cse

# To change the stream for all instances of the class we can change it directly from the class
CSStudent.stream = 'mech'

print(a.stream)    # prints ece
print(b.stream)    # prints mech

print(" - - - - -  -")
#