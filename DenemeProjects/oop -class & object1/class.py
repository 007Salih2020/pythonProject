# class definition
# class ClassName:
    # Statement

# object definition
#    obj = ClassName()
#    print(obj.atrr)

# # Python3 program to demonstrate instantiating  a class

class Dog():

    attr1 = 'mammal'
    attr2 = 'dog'

    # a simple method
    def fun(self):
        print("I am a self", self.attr1)
        print("I am a self", self.attr2)

# Driver code  Object instantiation
Rodger = Dog ()

#  # Accessing class attributes   and method through objects

print(Rodger.attr1)
Rodger.fun ()


# # sample class with init method

class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # sample method
    def say_hi(self):
        print("Hello, my name is ", self.name )

p=Person('Salih')
p.say_hi()

# # class declaration, class variables, constructor



class Dog:

	# Class Variable
	animal = 'dog'

	# The init method or constructor
	def __init__(self, breed, color):

		# Instance Variable
		self.breed = breed
		self.color = color


# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)


# # #
# we can create instance variable inside method

class Dog:

	# Class Variable
	animal = 'dog'

	# The init method or constructor
	def __init__(self, breed):

		# Instance Variable
		self.breed = breed

	# Adds an instance variable
	def setColor(self, color):
		self.color = color

	# Retrieves instance variable
	def getColor(self):
		return self.color


# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())


# #
