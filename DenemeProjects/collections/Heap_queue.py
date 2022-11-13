# represent priority queue

# heapify
import heapq



# initializing a list
li = [5,7,9,1,3]


# using heapify to convert list into heap

heapq.heapify(li)

# printing created heap

print("The created heap is: ", (list(li)))

print(" - - - - - - ")
#

## appending and popping items
# heappush (heap, ele)

# heappop(heap)
import heapq


# initializing a list
li = [5,7,9,1,3]


# using heapify to convert list into heap

heapq.heapify(li)

# printing created heap

print("The created heap is: ", end= "")
print(list(li))

# using heappush() to push elements into heap
# push 4

heapq.heappush(li,4)

# printing modified heap
print("The modified heap after push is:", end=" ")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is:", end=" ")
print(heapq.heappop(li))


print(" - - - - - - ")
# Adding and popping simultaneously
# heappushpop(heap, ele)
# heapreplace(heap, ele)

import heapq

# initializing list
li1=[5,1,9,4,3]

# initializing second list
li2=[5,7,9,4,3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
# pop2
print("the popped item using heappushpop() is :", end="")
print(heapq.heappushpop(li1,2))

# using heapreplace() to push and pop items simultaneously
# pop3
print("the popped iitem using heapreplace() is:", end=" ")
print(heapq.heapreplace(li2, 2))

print(" - - - - - - ")
#  find the largest and smallest elements from Heap
# nlargest(k, iterable, key=fun)   -> returns the largest elements
# nsmallest(k, iterable, key=fun) -> returns the smallest element
import heapq

# initializing list
li1= [6,7,9,4,3,5,8,10,1]

# using heapify() to convert list into heap
heapq.heapify(li1)

# using nlargest to print 3 largest numbers
print("the 3 largest numbers in list are:", end=" ")
print(heapq.nlargest(3,li1))

# using nsmallest to print 3 smallest numbers
print("the 3 smallest numbers in list are:", end=" ")
print(heapq.nsmallest(3,li1))


print(" - - - - - - ")
#
