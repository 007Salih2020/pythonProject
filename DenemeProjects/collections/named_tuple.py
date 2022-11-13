#
# NamedTuple - returns a tuple object with names for each position which the ordinary tuples lack

from collections import namedtuple

# declaring namedtuple
Student = namedtuple ('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Salih', '32', '20011991')

# Accessing using index
print("\nStudent age using index is : ", end="")
print(S[1])

# accessing using name
print("\nStudnet name using keyname is : ", end=" ")
print(S.name)


print("- -  -- - - ")

# Conversion Operations
# _make()   - is used to return a namedtuple() from iterable passed as argument
# _asdict() - returns OrderedDict() as constructed from mapped values of namedtuple()

from collections import namedtuple

# Declaring namedtuple
Student = namedtuple ('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Salih', '32', '20011991')

# initililzing iterable
li = ['Hamdi','23', '12031993']

# initializing dict
di={'name':"Salih", 'age':32, 'DOB':'20011991'}

# using _make() to return namedtuple()
print("\nThe namedtuple instance using iterable is:")
print(Student._make(li))

#using asdict() to return an OrderedDict()
print("\n OrderedDict instance usind nameduple is: ")
print(S._asdict())


print("- -  - - - -")
#  “**” (double star) operator :- This function is used to convert a dictionary into the namedtuple().

# Python code to demonstrate namedtuple() and
# _make(), _asdict() and "**" operator

# importing "collections" for namedtuple()
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student',
								['name', 'age', 'DOB'])

# Adding values
S = Student('Memo', '19', '2541997')

# initializing iterable
li = ['Ahmed', '19', '411997']

# initializing dict
di = {'name': 'Ömer', 'age': 19, 'DOB': '1391997'}

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is : ")
print(Student._make(li))

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is : ")
print(S._asdict())

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is : ")
print(Student(**di))

print("-  - - - -- - - -")
#
# _fields: This function is used to return all the keynames of the namespace declared.
# _replace(): _replace() is like str.replace() but targets named fields( does not modify the original values)

# Python code to demonstrate namedtuple() and
# _fields and _replace()

# importing "collections" for namedtuple()
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nazmi', '19', '2541997')

# using _fields to display all the keynames of namedtuple()
print("All the fields of students are : ")
print(S._fields)

# ._replace returns a new namedtuple, it does not modify the original
print("returns a new namedtuple : ")
print(S._replace(name='Namik'))
# original namedtuple
print(S)
