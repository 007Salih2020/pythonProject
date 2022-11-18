# Python program showing abstract base class work

from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass

class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 3 sides")

class Pentagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 5 sides")

class Hexagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 6 sides")

class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 4 sides")

# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

print("  - - - - - - - -")
#
# second example
# Python program showing abstract base class work

from abc import ABC, abstractmethod


class Animal(ABC):

    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")


class Snake(Animal):

    def move(self):
        print("I can crawl")


class Dog(Animal):

    def move(self):
        print("I can bark")


class Lion(Animal):

    def move(self):
        print("I can roar")


# Driver code
R = Human()
R.move()

K = Snake()
K.move()

L = Dog()
L.move()

M = Lion()
M.move()

print("  - - - - - - - -")
#

# Python program showing implementation of abstract  class through subclassing

import abc

class parent:
	def ozkans(self):
		pass

class child(parent):
	def ozkans(self):
		print("child class")

# Driver code
print( issubclass(child, parent))
print( isinstance(child(), parent))


print("  - - - - - - - -")
#
# using super()

# Python program invoking a
# method using super()

import abc
from abc import ABC, abstractmethod

class R(ABC):
	def al(self):
		print("Abstract Base Class")

class K(R):
	def al(self):
		super().al()
		print("subclass ")

# Driver code
r = K()
r.al()

print("  - - - - - - - -")
#

# Python program showing  abstract properties

import abc
from abc import ABC, abstractmethod


class parent(ABC):
    @abc.abstractproperty
    def alis(self):
        return "parent class"


class child(parent):

    @property
    def alis(self):
        return "child class"


try:
    r = parent()
    print(r.alis)
except Exception as err:
    print(err)

r = child()
print(r.alis)

print("  - - - - - - - -")
#

# Python program showing  abstract class cannot be an instantiation
from abc import ABC,abstractmethod

class Animal(ABC):
	@abstractmethod
	def move(self):
		pass
class Human(Animal):
	def move(self):
		print("I can walk and run")

class Snake(Animal):
	def move(self):
		print("I can crawl")

class Dog(Animal):
	def move(self):
		print("I can bark")

class Lion(Animal):
	def move(self):
		print("I can roar")

c=Animal()
