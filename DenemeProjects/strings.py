i =1

while (i<15):
    print(i)
    i+= 3

# iteration for loop
s = "hello world "

for i in s:
    print(i)

# iteration loop on list

L=[1,4,5,7,8,9]

for i in L:
    print(i)

#
for i in range(0,10):
    print(i)

# #
string1="GeeksForGeeks"
print(string1[0])
print(string1[-1])
print(string1[::-1])

string1="".join(reversed(string1))
print(string1)

print(string1[3:12])
print(string1[3:-2])

list1=list(string1)
list1[2]='p'
string2=''.join(list1)
print(string2)

string3= "{1} {0} {2}".format('geeks','for','life')
print(string3)

string4= "{0:.2f}".format(1/6)
print(string4)

string5= "|{:<20}|{:^30}|{:>40}".format('Geeks',
                                        'for',
                                        'Geeks')
print(string5)