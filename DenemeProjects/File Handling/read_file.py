# file should exist in the same directory as the python program file !

# file_object.read([n])
# file_object.readline([n])
# file_object.readlines()
'''
file1 = open("wiesbaden.txt", "w")
L= [" This is Wiesbaden \n", "This is the capital of Millionaire \n", "This is ancient city \n"]

# writing data to a file
file1.write("Hello \n")
file1.writelines(L)
file1.close() # to change fiel access modes

file1 = open ("wiesbaden.txt", "r+")

print("Output of read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth bite from the beginning

file1.seek(0)

print("Output of Readline function is")
print(file1.readline())
print()

file1.seek(0)

# to show difference between read and readline
print("outline of Read(9) function is")
print(file1.read(9))
print()

file1.seek(0)

print("Outline of Readline(9) function is")
print(file1.readline(9))
print()

file1.close()

print("Outline of Readlines function is")
print(file1.readlines())

print()

file1.close()
'''
print(" - - - - -")

#  with statement

L= ["This is Paris \n", "This is London\n", "This is Frankfurt\n"]

# creating a file
with open("wiesbaden.txt", "w") as file1:
    # writing date to a file
    file1.write("Hello \n")
    file1.writelines(L)
    file1.close()  # to change file access modes

with open("wiesbaden.txt", "r+") as file1:
    # reading from a file
    print(file1.read())
