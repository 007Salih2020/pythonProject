# iterating over list

list= ["geeks", "for", "jobs"]

for i in list:
    print(i)

# iterating over Dictiionary

print("Dictionary iteration")

d= dict()
d['xyz']=123
d['abc']=345

for i in d:
    print("% s % d" % (i,d[i]))

# # iterating over Dictiionary

print("String iteration")

s="Özkans"

for i in s:
    print(i)

# loop control statement
print("Loop Control flow")
# print all letters except "e" and "s"
for letter in "ÖzkansHause":
    if letter == "e" or letter == "s":
        continue
    print("Current Letter : ", letter)

# #  #

    if letter == "a " or letter == "u":
        break
    print("Current Letter : ", letter)