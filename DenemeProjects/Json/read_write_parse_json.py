#
# json.loads(json_string)
# Python program to convert JSON to Python


import json

# JSON string
employee ='{"id":"09", "name": "Sabri", "department":"Finance"}'

# Convert string to Python dict
employee_dict = json.loads(employee)
print(employee_dict)

print(employee_dict['name'])

print(" - - - - - - -  -- ")
# Python read JSON file

# json.load(file_object)

# Python program to read
# json file
''' 

import json

# Opening JSON file
f = open('/Users/ersa3094/PycharmProjects/pythonProject/DenemeProjects/Json/sample.json',)

# returns JSON object as a dictionary
data = json.load(f)

# Iterating through the json list
for i in data['emp_details']:
	print(i)

# Closing file
f.close()

'''
print(" - - - - - - -  -- ")
# Convert from Python to JSON

# json.dumps(dict, indent)

# Python program to convert Python to JSON


import json

# Data to be written
dictionary ={
"id": "04",
"name": "subhi",
"department": "HR"
}

# Serializing json
json_object = json.dumps(dictionary, indent = 4)
print(json_object)


print("-  - - - - - -")

# json.dump(dict, file_pointer)

# Python program to write JSON
# to a file


import json

# Data to be written
dictionary ={
	"name" : "sabri",
	"rollno" : 56,
	"cgpa" : 8.6,
	"phonenumber" : "9976770500"
}

with open("sample1.json", "w") as outfile:
	json.dump(dictionary, outfile)

