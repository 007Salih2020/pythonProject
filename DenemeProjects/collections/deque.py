# Deque  - Doubly ended queue - optimized list for quicker append and pop operations from both sides of the container.

from collections import deque

# declaring queue
queue = deque(['name', 'age', 'DOB'])

print(queue)


print("- - -  - - - - ")

# inserting elements
# inserting elements from both sides (left : appendleft(), right: append()

from collections import deque

de = deque([1,2,3])

# use append() to insert element at right end
de.append(4)

# printing modified deque
print("The deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
de.appendleft(6)

# printing modified deque
print("the deque after appending at left is :")
print(de)



print("- - -  - - - - ")

# removing elements
# elements can be removed from both sides - right: pop(), left: popleft()

from collections import deque

de= deque([6,1,2,3,4])

# using pop() to delete element from right end
de.pop()

# printing modified deque
print("the deque after deleting from right is:")
print(de)

# using popleft() to delete element from left
de.popleft()


print("the deque after deleting from left is:")
print(de)




print("- - -  - - - - ")

#Accessing Items in a deque
# index(ele, beg, end):- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
# insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
# remove():- This function removes the first occurrence of the value mentioned in arguments.
# count():- This function counts the number of occurrences of value mentioned in arguments.

# Python code to demonstrate working of
# insert(), index(), remove(), count()

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3, 3, 4, 2, 4])

# using index() to print the first occurrence of 4
print ("The number 4 first occurs at a position : ")
print (de.index(4,2,5))

# using insert() to insert the value 3 at 5th position
de.insert(4,3)

# printing modified deque
print ("The deque after inserting 3 at 5th position is : ")
print (de)

# using count() to count the occurrences of 3
print ("The count of 3 in deque is : ")
print (de.count(3))

# using remove() to remove the first occurrence of 3
de.remove(3)

# printing modified deque
print ("The deque after deleting first occurrence of 3 is : ")
print (de)

print(" - - - - - - - -")
# Different operations on deque
# extend(iterable):- This function is used to add multiple values at the right end of the deque. The argument passed is iterable.
# extendleft(iterable):- This function is used to add multiple values at the left end of the deque. The argument passed is iterable. Order is reversed as a result of left appends.
# reverse():- This function is used to reverse the order of deque elements.
# rotate():- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to the left. Else rotation is to right.

# Python code to demonstrate working of
# extend(), extendleft(), rotate(), reverse()

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3,])

# using extend() to add numbers to right end
# adds 4,5,6 to right end
de.extend([4,5,6])

# printing modified deque
print ("The deque after extending deque at end is : ")
print (de)

# using extendleft() to add numbers to left end
# adds 7,8,9 to left end
de.extendleft([7,8,9, 10])

# printing modified deque
print ("The deque after extending deque at beginning is : ")
print (de)

# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)

# printing modified deque
print ("The deque after rotating deque is : ")
print (de)

# using reverse() to reverse the deque
de.reverse()

# printing modified deque
print ("The deque after reversing deque is : ")
print (de)
