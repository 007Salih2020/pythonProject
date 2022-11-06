# using re.VERBOSE flag allows you to write more readable
import re
''' 
# without Verbose
regex_email = re.compile(r'^[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z\.]
                         re.IGNORECASE)

# with VERBOSE
regex_email = re.compile(r"""
                        ^[a-z0-9\.\.-]+)                    # local part
                        @                                   # single @ sign
                        ([a-z0-9\.-]+)                      # Domain Name
                        \.                                  # Single Dot (.)
                        ([a-z]{2,6})$                       # Top Level Domain 
                        """, re.VERBOSE | re.IGNORECASE)

'''
print("- - - - - - -")


# implementation of VERBOSE in RegEx

import re

def validate_email(email):
    regex_email = re.compile(r"""
                                °([a-z0-9_\.-]+)  
                                @
                                ([0-9a-z\.-]+)
                                \. 
                                ([a-z]{2,6})$
                            """, re.VERBOSE | re.IGNORECASE)

# regexObject is matched with the desidred string using fullmatch function.
# in case a match is found, search() returns MatchObject instance
    res=regex_email.fullmatch(email)

    if res:

        print("{} is Valid. Details are as follow:".format(email))

         # print first part/personal detail of Email ID
        print("Local: {}".format(res.group(1)))

         # print Domain Name of Email
        print("Domain : {}".format(res.group(2)))

        # print Top Level Domain. Name
        print("Top Level Domain:{}".format(res.group(3)))
        print()

    else:
        # if match not found
        print("{} is Invalid".format(email))

# Driver Code
validate_email("expectopatronun@gmail.com")
validate_email("ayadakedavra@yahoo.com@")
validate_email("Crucio@.com")

print("- - - - - - -")

#

