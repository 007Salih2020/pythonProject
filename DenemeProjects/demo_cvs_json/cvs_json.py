# convert cvs to json
'''
import csv
import json


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # Assuming a column named- listed- to be the primary key
            key = rows['name', 'source', 'destination', 'incoming Interface', 'outgoing Interface', 'comment', 'Date\ Created']
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


# Driver Code
# Decide the two file paths according to your computer system
csvFilePath = r'/Users/ersa3094/PycharmProjects/pythonProject/DenemeProjects/demo_cvs_json/Fortinet_rules.csv'
jsonFilePath = r'Names.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
'''
# # #  # # # #

import csv
import json


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        dialect = csv.Sniffer().sniff(csvf.readline(), delimiters=";")
        csvf.seek(0)
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf, dialect=dialect)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


csvFilePath = r'/Users/ersa3094/PycharmProjects/pythonProject/DenemeProjects/demo_cvs_json/Fortinet_rules.csv'
jsonFilePath = r'data.json'
csv_to_json(csvFilePath, jsonFilePath)