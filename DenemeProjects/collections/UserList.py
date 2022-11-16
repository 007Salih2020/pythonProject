# userList

from collections import UserList

L= [1,2,3,4]

# creating a userlist
userL = UserList(L)
print(userL.data)

# creating empty list
userL = UserList()
print(userL.data)


print("- - -  - -- ")
# another example

from collections import UserList

class MyList(UserList):

    # function to stop deletion from list
    def remove(self, s= None):
        raise RuntimeError("Deletion not allowed")

    # function to stop pop from list
    def pop(self, s= None):
        raise RuntimeError("Deletion not allowed")

# drivers code
L = MyList([1,2,3,4])

print("Original List")

# inserting to list
L.append(5)
print("After insertion")
print(L)

# deleting from list
L.remove()

print("- - -  - -- ")
#