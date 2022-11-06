# its primary function is to offer a search...

import re

s= ' I love Wiesbaden: nice place to live'

math = re.search(r'nice', s)

print('start index : ', math.start())
print('end index :', math.end())


print("- - -  - - -")
# \ - Backslash

import re

a = ' I live.in Frankfurt '

# without using \
math = re.search(r'.', a)
print(math)

# using \
math = re.search(r'\.', a)
print(math)



print("- - -  - - -")
# [] - Square Brackets

# ^- Caret
# $ - Dollar

# .-Dot

# | - or

# ? -Question

# *-Star

# + - Plus

# {} - Braces

# (<regex>) - Group

# special Sequences

# regex Module in Python

# re.findall()
# return all non-overlapping matches of pattern in string ....

import re
# a sample string where regular expression is searched
string = """ Hello my name is Salih 
              and my number is 123456 """
# a sample regular expression to find digits
regex = '\d+'

math = re.findall(regex, string)
print(math)


print("- - -  - - -")
# re.compile()

import re

# compile () creates regular expression character class [a-e], which is equivalent to [abcde].
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'
p = re.compile('[a-e]')

# findall() searches for the regular expression and return a list upon finding
print(p.findall("Alise, said Mr Salih "))



print("- - -  - - -")
# set class  [\s,.] will match any whitespace character, ','  or  '.'

import re

# \d is equivalent to [0-9]
p= re.compile('\d')
print(p.findall("I went  to him at 11 AM on 30th October 2022"))

# \d+ will match a group on [0-9], group of one or greater size
p = re.compile('\d+')
print(p.findall("I went  to him at 11 AM on 30th October 2022"))

print("- - -  - - -")
# another example

import re
# \w is equivalent to [a-zA-Z0-9_]
p = re.compile('\w')
print(p.findall("He said * in some_lang."))

# \W matches to non alphanumeric characters
p = re.compile('\W')
print(p.findall("He said *** in some_language. "))


print("- - -  - - -")
# example - 4

import re


# '*'  replaces the no. of occurrence of character

p = re.compile('ab*')

print(p.findall("ababbaabbb"))


print("- - -  - - -")
# re.split()

from re import split

# '\W+' denotes Non_Alphanumeric Characters or group of characters Upon finding ',' or whitespace '' , split (), splits the string

print(split('\W+','Words, words, Words'))
print(split('\W+', "Word's words Words"))

# here ':', '', ',' are non-alphanumeric thus the point where splitting occurs
print(split('\W+', 'On 12th Jan 2022, at 10:20 AM'))

# '\d+' denotes Numeric Characters or group of characters Splitting occurs at '12',  '2022', 11, 20 only

print(split('\d+', "On 12th Jan 2022, at 10:20 AM"))


print("- - -  - - -")
# another example for split

import re

print(re.split('\d+', "Hasan lives in Wiesbaden since 1st August 2017."))

# Boy and boy will be treated same when flags re.IGNORECASE

print(re.split('[a-f]+', "Aey, Boy oh boy, come here", flags=re.IGNORECASE))
print(re.split('[a-f]+', "Aey, Boy oh boy, come here"))

print("- - -  - - -")
# re.sub()

import re

# regex pattern 'ub' matches the string "Subject" and "Uber".
# as the CASE  has been ignored, using Flag, 'ub' should match twice with the string Upon matching,
# 'ub' is replaced by '~*' in "Subject", and in "Uber", 'Ub' is replaced

print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))

# consider the Case Sensitivity, 'Ub in "Uber", will not be replaced
print(re.sub('ub', '~~', 'Subject has Uber booked already'))

# as count has been given value 1, the maximum times replacement occurs is 1

print(re.sub('ub', '~*', "Subject has Uber booked already", count=1, flags=re.IGNORECASE))


# 'r' before the pattern denotes RE, \s is for start and end of a String
print(re.sub(r'\sAND\s', '&', 'Baked Beans And Spam', flags=re.IGNORECASE))


print(" - -  - - -")

# re.subn()

import re

print(re.subn('ub', '~*', 'Subject has Uber booked already'))

t= re.subn('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE)
print(t)
print(len(t))

# this will give smae output as sub() would have
print(t[0])

print("- - - - -")

# re.escape()

import re

# escape() returns a string with Backslash '\', before every Non-alphanumeric character

print(re.escape("This is Awesome even 1 AM"))
print(re.escape("I asked what is this [a-9], he said \t ^WOW"))

print("- - - - -")

# re.search()
import re

regex = r"([a-zA-Z]+)(\d+)"

math = re.search(regex, "I was born on June 24")

if match != None:

    print("Match at index %s, %s" % (match.start(), match.end()))

    print("Full match : %s" % (match.group(0)))

    print("Month : %s" % (match.group(1)))

    print("Day : %s" % (match.group(2)))

else:
    print("The regex pattern does not match ")


print("- - - - -")

#