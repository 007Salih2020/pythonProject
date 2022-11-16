#  UserSTring

from collections import UserString

d=12344

# creating an UserDict
user5=UserString(d)
print(user5.data)

# creating an empty UserDict

user5 = UserString("")
print(user5.data)

print("- - -  -")
# Anoter example

from collections import UserString

class MyString(UserString):

    # function to append to string
    def append(self, s):
        self.data += s
    # function to remove from string
    def remove(self, s):
        self.data = self.data.replace(s, "")

# drivers code
s1 = MyString("Wiesbaden")
print("Original String:", s1.data)
# appending to string
s1.append("k")
print("After Appending:", s1.data)

# removing from string
s1.remove("e")
print("After Removing:", s1.data)




print("- - -  -")
#

