# syntax class method
'''

Class C(object):
    @classmethod
    def fun(cls, arg1, arg2):

        ...
fun: function that needs to be converted into a class method
returns : a class method for function

'''

# # syntax static method

'''
class C(object):
    @staticmethod
    def fun(arg1, arg2):
    ...
return : a static method for function fun
'''

# example
from datetime import date

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('Hasan', 21)
person2 = Person.fromBirthYear('Hasan', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

print("- - - - - -")
# #