import operator

li = [1,2,3,4,5]

print("the original list is : ", end="")
for i in range (0, len(li)):
    print (li[i], end="")

print ("\r")

# set item to assign a new value to certain position
operator.setitem(li,3,2)

 # printing modified list
import operator
print("the original list is : ", end="")

for i in range (0, len(li)):
    print (li[i], end="")

print ("\r")

