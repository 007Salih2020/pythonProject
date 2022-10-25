# break statement

a= "arabaylagezdi"
b=0
for i in a:
    print(i)
    if i == "e" or i == "y":
        break
print("Out of for loop")
print()
i = 0


while True  :
    print(a[i])

    if a[i] == "e" or a[i] == "s":
        break
    i +=1
print("Out of while loop")

# # #

num=0
for i in range(10):
    num +=1
    if num == 8:
        break
    print(" the num has value :", num)

print("Out of Loop")
