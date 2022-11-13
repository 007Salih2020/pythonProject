#
import collections
from collections import ChainMap

d1={'a':1,'b':2}
d2={'c':3,'d':4}
d3={'e':5,'f':6}

# defining the chainmap
c= ChainMap(d1, d2, d3)

print(c)

print(" - -  - - -")
# keys, maps, values

from collections import ChainMap

dic1={'a':1,'b':2}
dic2={'c':3,'d':4}


# defining the chainmap
chain= collections.ChainMap(dic1, dic2)

# print chainMpa using maps
print("All the ChainMap contents are : ")
print(chain.maps)

# using values
print("All values of ChainMap are : ")
print(chain.values())

# using keys
print("All keys of ChainMap  are : ")
print(chain.keys())


print(" - - -- - - -")
#
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
print(chain1.maps)

# displaying value aasociated with be before reversing
print("Value asasociated with b before reversing is : ", end="")
print(chain1['b'])

# reverseing the ChainMap
chain1.maps = reversed(chain1.maps)

# displaing value aassociated with b after reversing
print("Value associated with b after reversing is :", end="")
print(chain1['b'])

print("- -  - - - -")
#
