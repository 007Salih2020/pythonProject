# a file with wiesbaden will be opened with the reading mode

file = open("wiesbaden.txt", 'r')

for each in file:
    print(each)

print(" - - - - -")

# another way to open the file and read

file = open("wiesbaden.txt", "r")
print(file.read())

print(" - - - - -")

# read with limited number of characters

file = open ("Wiesbaden.txt", "r")
print(file.read(15))

print(" - - - - -")

# creating a file with write mode

file = open ("Mainz.txt", "w")
file.write("This is the another capital city")
file.write("\n it is across the river ")
file.close()

print(" - - - - -")

# working with append mode

file = open("Wiesbaden.txt", 'a')
file.write("\n there are too many government institutions here")
file.close()

print(" - - - - -")

# auto clean-up

with open("Mainz.txt") as file:
    data = file.read()
# do something with data :-)

print(" - - - - -")

# using write with with() function

with open("Wiesbaden.txt", "w") as f:
    f.write("Hello World ! ! !")


print(" - - - - -")

#  split()

with open("Mainz.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

print(" - - - - -")

#