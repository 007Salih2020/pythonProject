# create set in python
set1=()
print("initial blank set: ")
print(set1)

# use of a String
set1=set("geeks for geeks")
print("\nSet with the use of String:")
print(set1)

# use of Constructor
String='Geeks for Geeks'
set1=set(String)
print("\nSet with the use of Object:")
print(set1)

# use of a List
set1 = set(["Geeks", "for", "Geeks"])
print("\nSet with the use of List:")
print(set1)

# having doublicated values
set1=set([1,2,4,4,3,3,3,6,5])
print("\nSet with the use of Numbers:")
print(set1)

# having numbers and strings
set1=set([1,2,'Geeks',4,'For',6,'Geeks'])
print("\nSet with the use of Mixed Values:")
print(set1)

# set containing numbers
my_set={1,2,3}
print(my_set)

# addition
set1.add(8)
set1.add(9)
set1.add((6,7))
print("\nSet after Addition 3 Elements:")
print(set1)

# using iterator
for i in range(1,6):
    set1.add(i)
print("\nSet after Addition of Elements from 1-5:")
print(set1)

# using update function
set1=set([4,5,(6,7)])
set1.update([10,11])

print("\nSet after Addition of Elements using Update: ")
print(set1)

# accessing element using for loop
print("\nElements of set:" )
for i in set1:
    print(i,end=" ")

# using in keyword
print("Geeks" in set1)

# using remove()  & discard ()

