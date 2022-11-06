# counter is a container included in the collection modules.
# what is container?
# objects which hold other objects. examples, Tuple, List and Dictionar
# container is a sub-class of dict.

# initializing Counter Objects

from collections import Counter

# with sequence of items
print(Counter(['B','B', 'A', 'B', 'C', 'A','B', 'B','A', 'C']))

# with dictionary

print(Counter({'A':3, 'B':5, 'C':2}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))


print(" _ _ _ _ _ _ _")
# with update() method, you may update

from collections import Counter

coun = Counter()

coun.update([1,2,3,1,2,1,1,2])
print(coun)

coun.update([4,11])
print(coun)

print("- - - - - -")
#
# subract() method ile cikartili

from collections import Counter

c1= Counter(A=4, B=3, C=10)
c2= Counter(A=10, B=3, C=4)

c1.subtract(c2)
print(c1)

print(" - - -- - - -")
#

from collections import Counter

# create list
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']

# count distinct elements and print Counter object
print(z)
print(Counter(z))




print(" - - -- - - -")
#