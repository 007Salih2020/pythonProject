
# importing the csv module
import csv
import json

# my data rows as dictionary objects
mydict = [{'branch': 'COE', 'cgpa': '9.0',
           'name': 'Salih', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1',
           'name': 'Sabit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3',
           'name': 'Adiye', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5',
           'name': 'Sakar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8',
           'name': 'Pamuk', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1',
           'name': 'Sakine', 'year': '2'}]

# field names
fields = ['name', 'branch', 'year', 'cgpa']

# name of csv file
filename = "university_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(mydict)

print(" - - - - - -  - -")
#