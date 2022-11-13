# Normally, Dictionary in Python is unordered collection.
# dictionary holds key-value pair.
# key is unique and immutable

Dict ={1:'Wiesbaden', 2:'nice', 3:'city'}
print("Dictionary")
print(Dict)
print(Dict[1])



print(" - - -- - - -")
# sample defaultdict

from collections import defaultdict

def def_value():
    return "Not At the Moment"

# defining the dict
d = defaultdict(def_value)
d['a']= 1
d['b']=2

print(d['a'])
print(d['b'])
print(d['c'])




print(" - - -- - - -")
#

# inner Working of defaultdict
# defaultdict adds one writable instance variable and none mthoed in addition to the standard dictionary operations.
# default_factory parameter and the method providing is __missing__

from collections import defaultdict

# defining the dict and passing lambda as default_factory argument
d = defaultdict(lambda : "Not present")
d['a']=1
d['b']=2

print(d['a'])
print(d['b'])
print(d['c'])




print(" - - -- - - -")
#
# __missing__()  this function is used to provide the default value for the dictionary.
# this function takes default_factory as an argument and if this argument is None, a KeyError is raised
# this method is basically called __getitem__()

from collections import defaultdict

# defining the dict and passing lambda as default_factory argument
d = defaultdict(lambda : "Not present")
d['a']=1
d['b']=2

print(d.__missing__('a'))
print(d.__missing__('d'))

print(" - - -- - - -")
#
# using List as default_factory

from collections import defaultdict

d=defaultdict(list)

for i in range(5):
    d[i].append(i)

print("Dictionary with values as list: ")
print(d)

print(" - - -- - - -")
#

# using int as default_factory

from collections import defaultdict
# defining dict

d = defaultdict(int)

L = [1,2,3,4,2,4,1,2]

# iterate through the list  for keeping the count

for i in L:

    # default value is 0 so there si no need to enter the key first
    d[i] += 1

print(d)
