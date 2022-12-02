# update()

# Python program to update
# JSON


import json

# JSON data:
x =  '{ "organization":"IHK",
        "city":"Wiesbaden",
        "country":"Germany"}'

# python object to be appended
y = {"pin":1001}

# parsing JSON string:
z = json.loads(x)

# appending the data
z.update(y)

# the result is a JSON string:
print(json.dumps(z))

print(" - - - - - - -")
#

# Python program to update
# JSON


import json

# function to add to JSON


def write_json(new_data, filename='sample.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


# python object to be appended
y = {"emp_name": "Mikail",
     "email": "Mikail@gmail.com",
     "job_profile": "Full Time"
     }

write_json(y)
