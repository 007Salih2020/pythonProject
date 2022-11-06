# inherit the capacity of another class

# demonstrate interitance

class Person(object):

    # constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # to check if this person is an employee
    def Display(self):
        print(self.name, self.id)

# driver code
emp = Person ("Salih", 12)  # an Object of Person
emp.Display()

print(" - - - - -  -")
#  creating child class

class Emp(Person):

    def Print(self):
        print("* Emp class called ")

Emp_details = Emp("Osman", 13)
Emp_details.Display()
Emp_details.Print()

print(" - - - - -  -")
# base and super class  + obj in bracket

class Person(object):

    def __init__(self, name):
        self.name = name
    # to get the name
    def getName(self):
        return self.name

    # to check if this person is an employee
    def isEmployee(self):
        return False
print(" - - - - -  -")
# inherited or Subclass (Note person in bracket)
class Employee(Person):

    # here we return true
    def isEmployee(self):
        return True

# Driver code
emp = Person("Sabir1") # an Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Sabir2") # an Object of Employee
print(emp.getName(), emp.isEmployee())

print(" - - - - -  -")
# #  #
# demonstrate how parent constructors are called

# parent class
class Person(object):
    # init is know as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


print(" - - - - -  -")

# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init_ of the parent class
        Person.__init__(self, name, idnumber)

# creation of an object variable or an issue
a = Employee('Osman', 2312, 3453, "Intern")

# calling a  function of the class Person using its instance
a.display()

print(" - - - - -  -")
# #  #
# if you forget to invoke __init__ of the parent clas, produces error
'''  
class A:

    def __init__(self, n="Salih"):
        self.name = n

class B(A):

    def __init__(self, roll):
        self.roll = roll

object = B(23)
print(object.name)
'''
print(" - - - - -  -")
#  different type of inheritance : single (as above) and multiple
# example for multiple inheritance

class Base1(object):
    def __init__(self):
        self.str1 = "Wiesbaden"
        print("Base1")

class Base2(object):
    def __init__(self):
        self.str2 = "Mainz"
        print("Base2")

class Derived(Base1, Base2):
    def __init__(self):

        # calling constructors of Base1 and Base2
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)

obj = Derived()
obj.printStrs()

print(" - - - - -  -")
# child and grandchild relationship

class Base(object):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

# inherited or Sub Class (Note - Person in bracket)

class Child(Base):

    def __init__(self, name, age):

        Base.__init__(self, name)
        self.age = age

    # to get name
    def getAge(self):
        return self.age

# inherited or sub-class
class GrandChild(Child):

    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def getAddress(self):
        return self.address

g = GrandChild("Erkan", 17, "Albany")
print(g.getName(), g.getAge(), g.getAddress())

print(" - - - - -  -")
# Private members of the parent class

class C(object):

    def __init__(self):
        self.c = 21

        # d is private instance variable
        self.__d =42

class D(C):

    def __init__(self):
        self.e = 84
        C.__init__(self)

object1 = D()
print(object1.d)

print(" - - - - -  -")

# since 'd' is made private by those underscores(line-185), it is not available