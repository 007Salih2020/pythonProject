# python code to demonstrate working of enumerate()

for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key, value)

# working of enumerate

for key, value in enumerate(['working', 'for', 'alone',
                             'is', ' the', ' big',
                             'coding', 'place']):
    print(key,value, end=":")

# working of zip

questions = ['name','colour','shape']
answers=['apple','red','circle']

for questions, answers in zip (questions,answers):
    print('\nwhat is your {0}? I am {1}.'.format(questions, answers))

# working of items

d={"apple":"wiesbaden", "banana":"gana"}

print("\nthe key value pair using items is: ")
for i,j in d.items():
    print(i,j)

# working of items 2#
king= {"Akbar":"great", "chandragupta":"the maurya", "Modi": "the Cahrger"}

for key, value in king.items():
    print(key,value)

# working of items sorted 1

lis= [1,2,3,4,5,6,2,4]
print("\nthe list in sorted order is :")

for i in sorted(set(lis)):
    print(i, end=" ,")

# # working of items sorted 2

basket= ["guave", "orange", "apple", "pear", "guava", "banana", "grape"]

for fruit in sorted(set(basket)):
    print(fruit)

# working reversed

lis=[1,3,4,5,2,9,3]

print("\n the list in reversed order is:")
for i in reversed(lis):
    print(i, end=" ")

# working reversed 2

for i in reversed(range(0,20,5)):
    print(i)

#