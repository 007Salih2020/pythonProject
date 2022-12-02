#
# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="user",
    passwd ="password"
)

print(dataBase)

# Disconnecting from the server
dataBase.close()

print(" - - - - - - - - - - - -")
#

