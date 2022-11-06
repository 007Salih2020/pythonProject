# sample for re.search

import re

regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "I was born on June 24")

if match != None:

    print("Match at index %s, %s" % (match.start(), match.end()))

    print("Full match : %s" % (match.group(0)))

    print("Month : %s" % (match.group(1)))

    print("Day: %s" % (match.group(2)))

else:
    print("The regex pattern does not match")


print("- - -  -")

# sample for re.findall()

import re

string = """ 
        Hello my number is 12345
        and my friends number is 13579 """

regex = '\d+'

match = re.findall(regex, string)
print(match)


print("- - -  -")

#
