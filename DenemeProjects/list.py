List=[1,2,3,4,5,6,]
print(List)

list_mix=[1,2,'geeks',4,'for',6,'geeks']
print(list_mix)

print(List[0])

print(list_mix[2])

# multi dimensional list
list_md=[["geeks","for","day"],["Geeks","two"]]

print(list_md[0][2])
print(list_md[1][1])
print(len(list_md))
print(len(list_mix))
print(len(List))

'''  
# input the list as string
string = input("Enter elements (space-seperated): ")
lst=string.split()
print('the list is: ', lst)  # printing the list

# input size of hte list

n=int(input("enter the size of list: "))
lst1=list(map(int, input("enter the integer elements: ").strip().split(',')))[ :n]

print('the list is : ', lst1)
'''

# adding elements to list
list2=[]
print(list2)

list2.append(1)
list2.append(2)
list2.append(3)
print(list2)

# using iterator
for i in range(4,7):
    list2.append(i)
print(list2)

# add additional elements
list2.append((7,8))
print(list2)
list5=['for','geeks']
list2.append(list5)
print(list2)