#

print("- - -  - - - - - - ")
#
import json
# Json string
employee='{"id":"09", "name":"Salih", "department":"Professional Delivery"}'

# convert string to Python dict
employee_dict = json.loads(employee)
print(employee_dict)
print(type(employee_dict))
print("\n")

# convert Python dict to Json

json_object = json.dumps(employee_dict, indent=4)
print(json_object)
print(type(json_object))

print("- - -  - - - - - - ")
#
## working with Json Data in Python

# python program showing use of json package
import json

# {key:value mapping}
a = {
    "name":"Sabri",
    "age":31,
    "Salary":25000
}
# conversion to Json done by dumps() function
b= json.dumps(a)
# printing the output
print(b)

print("- - -  - - - - - - ")
# Another example for Array conversion

import json
# list conversion to Array
print(json.dumps(['welcome', "to", "wiesbaden"]))

# tuple conversion to Array
print(json.dumps(("welcome", "to", "Frankfurt")))

#string conversion to String
print(json.dumps("Hi"))

# int conversion to Number
print(json.dumps(1234))

# float conversion to number
print(json.dumps(23.234))

# Boolean conversion to their respective values
print(json.dumps(True))
print(json.dumps(False))

# none value to null
print(json.dumps(None))

print("- - -  - - - - - - ")
#
## serializing Json = encoding
''' 
with open("smaple.json", "w") as p:
    json.dump(var,p)


print("- - -  - - - - - - ")
#

## open the file in read mode

with open("sample.json", "r") as read_it:
	data = json.load(read_it)


print("- - -  - - - - - - ")
#

## Deserialization
json_var ="""
{
	"Country": {
		"name": "INDIA",
		"Languages_spoken": [
			{
				"names": ["Hindi", "English", "Bengali", "Telugu"]
			}
		]
	}
}
"""
var = json.loads(json_var)


print("- - -  - - - - - - ")
#

## Encoding & Decoding
### demjson should be installed
# example -  for Encoding

# storing marks of 3 subjects
var = [{"Math": 50, "physics":60, "Chemistry":70}]
print(demjson.encode(var))
 
print("- - -  - - - - - - ")
#
## example - decode

var = '{"a":0, "b":1, "c":2, "d":3, "e":4}'
text = demjson.decode(var)

print("- - -  - - - - - - ")
#
## example - iterencode package

# Other Method of Encoding
json.JSONEncoder().encode({"foo": ["bar"]})
'{"foo": ["bar"]}'

# Using iterencode(object) to encode a given object.
for i in json.JSONEncoder().iterencode(bigobject):
	mysocket.write(i)


print("- - -  - - - - - - ")
#
## example -  Encoding and Decoding using dumps() and loads().

# To encode and decode operations
import json
var = {'age':31, 'height':6}
x = json.dumps(var)
y = json.loads(x)
print(x)
print(y)

# when performing from a file in disk
with open("any_file.json", "r") as readit:
	x = json.load(readit)
print(x)

print("- - -  - - - - - - ")
#
## Command Line Usage

# The JSON library can also be used from the command-line, to validate and pretty-print your JSON.

#  $ echo "{ \"name\": \"Monty\", \"age\": 45 }"
'''
print("- - -  - - - - - - ")
#
## Searching through JSON with JMESPath

# JMESPath is a query language for JSON. It allows you to easily obtain the data you need from a JSON document.
# If you ever worked with JSON before, you probably know that it’s easy to get a nested value. For example,
# doc[“person”][“age”] will get you the nested value for age in a document.

print("- - -  - - - - - - ")
#
### Real World example
import requests
import json

# Now we have to request our JSON data through
# the API package
res = requests.get("https://jsonplaceholder.typicode.com / todos")
var = json.loads(res.text)

# To view your Json data, type var and hit enter
var

# Now our Goal is to find the User who have
# maximum completed their task !!
# i.e we would count the True value of a
# User in completed key.
# {
	# "userId": 1,
	# "id": 1,
	# "title": "Hey",
	# "completed": false, # we will count
						# this for a user.
# }

# Note that there are multiple users with  unique id, and their task have respective  Boolean Values.

def find(todo):
	check = todo["completed"]
	max_var = todo["userId"] in users
	return check and max_var

# To find the values.

Value = list(filter(find, todos))

# To write these value to your disk

with open("sample.json", "w") as data:
	Value = list(filter(keep, todos))
	json.dump(Value, data, indent = 2)
