# collections.UserDict([])

from collections import UserDict

d = {
    'a':1,
    'b':2,
    'c':3
}

# creating an UserDict
userD = UserDict(d)
print(userD.data)

# creating an empty UserDict
userD = UserDict()
print(userD.data)


print(" - - - - - - ")
# Second Example

from collections import UserDict

# creating Dictionary where deletion is not allowed

class MyDict(UserDict):

    # function to stop deletion from dictionary
    def __del__(self):
        raise RuntimeError ("Deletion not allowed")

    # function to stop pop from dictionary
    def pop(self, s= None):
        raise RuntimeError ("Deletion not allowed")

    # function to stop popitem from dictionary
    def popitem(self, s=None):
        raise RuntimeError ("Deletion not allowed")

# drivers code
d= MyDict({
    'a': 1,
    'b': 2,
    'c': 3
})

print("Original Dictionary")
print(d)

d.pop(1)


print(" - - - - - - ")
#
