#
# importing the csv module
import csv

# field names
fields = ['Name', 'Email']

# data rows of csv file
rows = [['Salih', 'salihl.rbg@gmail.com'],
        ['Sacit', 'sacit.ef@gmail.com'],
        ['Adiya', 'adiya.df@gmail.com'],
        ['Sakar', 'sakar.erfg@gmail.com'],
        ['Pamuk', 'pamuk.efg@gmail.com'],
        ['Sahil', 'sahil.gfg@gmail.com']]

# name of csv file
filename = "email_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)

print(" - - -  - - - - ")
#

