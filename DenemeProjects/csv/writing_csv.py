#
# importing the csv module
import csv

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [['Salih', 'COE', '2', '9.0'],
        ['Ahmed', 'COE', '2', '9.1'],
        ['Yusuf', 'IT', '2', '9.3'],
        ['Sabri', 'SE', '1', '9.5'],
        ['Pamuk', 'MCE', '3', '7.8'],
        ['Saygi', 'EP', '2', '9.1']]

# name of csv file
filename = "university_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)

print(" - - - - - - - ")
#
##
