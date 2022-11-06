# re.match()

# A Python program to demonstrate working of re.match().
import re

# Lets use a regular expression to match a date string
# in the form of Month name followed by day number
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 24")

if match != None:

	# We reach here when the expression "([a-zA-Z]+) (\d+)"  matches the date string.
    # This will print [14, 21), since it matches at index 14 and ends at 21.
	print ("Match at index %s, %s" % (match.start(), match.end()))

	# We us group() method to get all the matches and captured groups. The groups contain the matched values.
	# In particular:  match.group(0) always returns the fully matched stringmatch.group(1) match.group(2), ...
    # return the capture  groups in order from left to right in the input string
	# match.group() is equivalent to match.group(0)

	# So this will print "June 24"
	print ("Full match: %s" % (match.group(0)))

	# So this will print "June"
	print ("Month: %s" % (match.group(1)))

	# So this will print "24"
	print ("Day: %s" % (match.group(2)))

else:
	print ("The regex pattern does not match.")


print("- - - - -")

# matching a pattern with Text
# re.match(pattern, string, flags=0)

import re

def findMonthAndDate(string):
    regex= r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)

    if match == None:
        print("Not a valid date")
        return

    print("Given Data :%s" % (match.group()))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))

# Driver Code
findMonthAndDate("June 24")
print("")
findMonthAndDate("I was born on June 24")


print("- - -  -")

# re.findall()

import re
string = """ Hello my NUmber is 123456
                and my friend's number is 13579 """

# a sample regular expression to find digits
regex= '\d+'

match = re.findall(regex, string)

print(match)


print("- - -  -")

#




print("- - -  -")

#