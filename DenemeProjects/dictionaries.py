# basic dictionary
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)

# # Creating a Dictionary  with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\n Dictionary with the use of Mixed Keys: ")
print(Dict)

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

#  Creating a Nested Dictionary as shown in the below image
Dict = {1: 'Geeks', 2: 'For',
         3: {'A': 'Welcome', 'B': 'To', 'C': 'Hous'}}
print(Dict)

# # Creating a Dictionary
Dict1 = {1: 'Geeks', 'name': 'For', 3: 'jobs'}

# accessing a element using key
print("Accessing a element using key:")
print(Dict1['name'])

# accessing a element using key
print("Accessing a element using key:")
print(Dict1[1])
print(Dict1[3])

#  accessing a element using get() method
print("Accessing a element using get:")
print(Dict.get(3))
print(Dict1.get(3))

# demo for all dictionary methods
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

# copy() method
dict2 = dict1.copy()
print(dict2)

# clear() method
dict1.clear()
print(dict1)

# get() method
print(dict2.get(1))

# items() method
print(dict2.items())

# keys() method
print(dict2.keys())

# pop() method
dict2.pop(4)
print(dict2)

# popitem() method
dict2.popitem()
print(dict2)

# update() method
dict2.update({3: "Scala"})
print(dict2)

# values() method
print(dict2.values())
