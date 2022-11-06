# single inheritance

#base class
class Parent:

    def func1(self):
        print("this function is in parent class.")

# derived class
class Child(Parent):

    def func2(self):
        print(" this function is in child class. ")

# Drivers code
object = Child()
object.func1()
object.func2()

print(" - - - - - -")
# # #

# multiple inheritance

# base class1
class Mother:
    mothername = " "

    def mother(self):
        print(self.mothername)

# base class2
class Father:
    fathername=" "

    def father(self):
        print(self.fathername)

# another class
class Son(Mother, Father):

    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

# Drivers code
s1 = Son()
s1.mothername= "Elisa"
s1.fathername= "Isak"
s1.parents()


print(" - - - - - -")
# Multi-level inheritance

# base class
# Python program to demonstrate
# multilevel inheritance

# Base class


class Grandfather:

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

# Intermediate class


class Father1(Grandfather):
	def __init__(self, fathername1, grandfathername):
		self.fathername1 = fathername1

		# invoking constructor of Grandfather class
		Grandfather.__init__(self, grandfathername)

# Derived class


class Son(Father1):
	def __init__(self, sonname, fathername1, grandfathername):
		self.sonname = sonname

		# invoking constructor of Father class
		Father1.__init__(self, fathername1, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername1)
		print("Son name :", self.sonname)


# Driver code
s1 = Son('Haci', 'Abdullah', 'Hasan Hüseyin')
print(s1.grandfathername)
s1.print_name()



print(" - - - - - -")
# # Hierarchical Inheritance

# base class
class Parent:
    def func1(self):
        print("this function is in parent class")

# derived class1
class Child1(Parent):
    def func2(self):
        print("this function is in Child 1")

# Derived class 2
class Child2(Parent):
    def func3(self):
        print("This function is in Child 2")

# Drivers code

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

print(" - - - - - -")

#  Hybrid Inheritance

class School:
    def func1(self):
        print("This function is in School !")

class Student1(School):
    def func2(self):
        print("This function is in Student 1")

class Student2(School):
    def func3(self):
        print("This function is in Student 2")

class Student3(Student1, Student2):
    def func4(self):
        print("This function is in  Student 3")

# Drivers Code
object = Student3()
object.func1()
object.func2()

#