# protected members

class Base:

    def __init__(self):

        # protected member
        self._a=2

# creating derived class
class Derived(Base):

    def __init__(self):

        # calling constructor of base class
        Base.__init__(self)
        print("Calling protected member of base class: ", self._a)

        # modify the protected variabla
        self._a=3
        print("Calling modified protected member outside class: ", self._a)

obj1= Derived()
obj2=Base()

# calling protected mmember
# can be accessed but should not be done due to convention
print("Accessing protected member of obj1 : ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2 : ", obj2._a)

print(" - - -  -")

 # # #

 # private members

class Base1:

     def __init__(self):
         self.a = "I love Wiesbaden"
         self._c= "I love Wiesbaden"

class Derived(Base1):
    def __init__(self):

        # calling constructor of base class
        Base1.__init__(self)
        print("Calling private member of base class :")
        print(self._c)

# Driver code
obj1 = Base1()
print(obj1.a)

# print(obj1.c) will raise an Attribute Error
# Uncommenting obj2 = Derived() will also raise an AttributeError as private member of base class is called inside derived class



print(" - - -  -")
#
