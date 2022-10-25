# while loop

count=2
while (count < 7):
    count = count + 2
    print("Hi, there")

# run the list until there is an element present in the list
a=[1,2,3,4]
while a:
    print(a.pop())

# Single statement while block

count=0
while (count<3): count+=1; print("Hello Salih")

# print every letter except "e" and "s"
i =0
a = "Salih bugun eve geldi"

while i< len(a):
    if a[i] == 'e' or a[i] == 's':
        i+=1
        continue
    print("current letter :", a[i])
    i += 1

# break the loop as soon as see the given letters

i=0
a="Johannes bugun arabaya bindi"

while i< len(a):
    if a[i] == "e" or a[i] == "s":
        i +=1
        break
    print("Current letter :", a[i])
    i+=1

# empty loop

a="Erkan evde oyun oynadi"
i=0

while i< len(a):
    i += 1
    pass
print ("Value of i :", i)

# while loop with else

i = 0
while i < 4:
    i += 1
    print(i)
else:
    print("No Break \n")

i=0
while i< 4:
    i += 1
    print(i)
    break
else:
    print("No Break")


# sentinel Controlled Statement

a = int (input("Enter a number (-1 to quit):"))

while a != -1:
    a = int(input("Enter a number (-1 to quit):"))

#