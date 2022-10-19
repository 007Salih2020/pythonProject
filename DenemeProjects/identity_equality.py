# equality operator
a=10
b=10

#return true because both a and b is have same value
print(a==b)
  # outcome True

# return True b/c both a and b is pointing to the same object
print(id(a))
  # outcome  140250278193744

c = a

print(id(c))

# outcome  140250278193744

list1= []
list2 = []
list3 = list1

#case 1
if (list1 == list2):
    print("True")
else:
    print("False")

# case 2

if (list1 is list2):
    print("True")
else:
    print("False")

# case 3
if (list1 is list3):
    print("True")
else:
    print("False")

# case 4
list3 = list3 + list2
if (list1 is list3):
    print("True")
else:
    print("False")

