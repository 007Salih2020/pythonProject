# there are too many collections, which runs as containers

# Counters = it is used to count of the elements in an iterable in the form of an unordered dictionary

# initializing Counter Objects

from collections import Counter

# with sequence of items
print(Counter(['B','B', 'A', 'B', 'C', 'A','B', 'B','A', 'C']))

# with dictionary

print(Counter({'A':3, 'B':5, 'C':2}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))


print(" _ _ _ _ _ _ _")
#

# OrderedDict -  sub-class of dictionary but unlike dictionary, it remembers the order in wiht the keys were inserted

from collections import OrderedDict

d={}
d['a']=1
d['b']=2
d['c']=3
d['d']=4

for key, value in d.items():
    print(key, value)

print("\n This is an Ordered Dict: \n")

od = OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4

for key, value in od.items():
    print(key, value)


print("-  - - -  -")

# example : deleting and re-inserting


from collections import OrderedDict



print("\n This is an Ordered Dict: \n")

od = OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4

print("Before Deleting: ")

for key, value in od.items():
    print(key, value)

# deleting element
od.pop('a')

# re-inserting the same
od['a']=1

print("\n After re-inserting: ")

for key, value in od.items():
    print(key, value)

print("-  - - -  -")

# DefaultDict

from collections import defaultdict

# defining dict

d = defaultdict(int)

L = [1,2,3,4,2,4,1,2]

# iterate through the list  for keeping the count

for i in L:

    # default value is 0 so there si no need to enter the key first
    d[i] += 1

print(d)

print(" - - - - -")

# another example

from collections import defaultdict

d = defaultdict(list)

for i in range(5):
    d[i].append(i)

print("Dictionary with values as List :")
print(d)

print("- -  - - -")

# ChainMap - encapsulates many dictionares into a single unit and returns a list of dictionaries

#
from collections import ChainMap

d1={'a':1,'b':2}
d2={'c':3,'d':4}
d3={'e':5,'f':6}

# defining the chainmap
c= ChainMap(d1, d2, d3)

print(c)

print(" - -  - - -")
# Accessing key and values from chainmap

from collections import ChainMap

d1={'a':1,'b':2}
d2={'c':3,'d':4}
d3={'e':5,'f':6}

# defining the chainmap
c= ChainMap(d1, d2, d3)

# Accessing Values using key name
print(c['c'])

# accessing values using values() method
print(c.values())

# accessing keys using keys() method
print(c.keys())

print("- - - - - ")
#  Adding new dictionary

# new_child()

import collections

# initilazing dictionaries
dic1 = {'a':1,'b':2}
dic2 = {'c':3,'d':4}
dic3 = {'e':5,'f':6}

# initializing ChainMap
chain = collections.ChainMap(dic1,dic2)

# printing chainMap
print("\nAll the ChainMap contents are :")
print(chain)

# using new_child() add new dictionary
chain1 = chain.new_child(dic3)

# printing chainMap
print("\nDisplaying new ChainMap:")
print(chain1)

print("- -  - - - -")

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

# Deque  - Doubly ended queue - optimized list for quicker append and pop operations from both sides of the container.

from collections import deque

# declaring queue
queue = deque(['name', 'age', 'DOB'])

print(queue)


print("- - -  - - - - ")

# inserting elements
# inserting elements from both sides (left : appendleft(), right: append()

from collections import deque

de = deque([1,2,3])

# use append() to insert element at right end
de.append(4)

# printing modified deque
print("The deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
de.appendleft(6)

# printing modified deque
print("the deque after appending at left is :")
print(de)



print("- - -  - - - - ")

# removing elements
# elements can be removed from both sides - right: pop(), left: popleft()

from collections import deque

de= deque([6,1,2,3,4])

# using pop() to delete element from right end
de.pop()

# printing modified deque
print("the deque after deleting from right is:")
print(de)

# using popleft() to delete element from left
de.popleft()


print("the deque after deleting from left is:")
print(de)




print("- - -  - - - - ")

# UserDict - dictionary -> like container act as a wrapper around the dictionary objects.
# the best practice, when someone wants to create his own dict
''' 
from collections import UserDict

# create a dictionary where deletion is not allowed
class MyDict(UserDict):

    # function to stop deletion from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")

    # function to stop pop from dictionary
    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")

    # function to stop popitem from dict
    def popitem(self, s = None):
        raise RuntimeError("Deletion not allowed")

# drivers code
d = MyDict({'a':1,
            'b':2,
            'c':3})

d.pop()
'''

print("- - -  - - - - ")

# UserList - like container , acts as a wrapper around the list objects
'''
from collections import UserList

class MyList(UserList):

    #function to stop deletion from list
    def remove(self, s = None):
        raise RuntimeError("Deletion not allowed")

    # function to stop pop from List
    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")

# drivers code
L = MyList([1,2,3,4])

print("Original List")

# inserting list
L.append(5)
print("After insertion")
print(L)

# deleting from list
L.remove()

'''

print("- - -  - - - - ")

# UserString - like container , like UserDict & UserList, acts as a wrapper around string object

from collections import UserString

class MyString(UserString):

    # function to append to string
    def append(self,s):
        self.data += s

    # function to remove from string
    def remove(self,s):
        self.data = self.data.replace(s, "")

# drivers code
s1 = MyString("Wiesbaden")
print("Original string: ", s1.data)

# appending to string
s1.append("s")
print("String After Appending: ", s1.data)

# removing from string
s1.remove("e")
print("String after removing :", s1.data)


print("- - -  - - - - ")

#

