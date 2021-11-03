import os

import mysql.connector
from dotenv import load_dotenv

# setup database
load_dotenv()
db = mysql.connector.connect(host=os.getenv("HOST"), user=os.getenv("USER"), passwd=os.getenv("PASSWD"),
                             database=os.getenv("DATABASE"))
mycursor = db.cursor()

'''
    Link: https://leetcode.com/problems/combine-two-tables/
    Purpose: Report the firstName, lastName, city, and state of each person in the Person table. 
           : If the address of a personId is not present in the Address table, report null instead.
    parameter: none
    return: none
    Pre-Condition: none
    Post-Condition: none
'''


def combineTwoTables():
    print("\n+===== Answer =====+")
    mycursor.execute(
        "SELECT firstName, lastName, city, state From Person LEFT OUTER JOIN Address ON Person.personId=Address.personId")
    for data in mycursor:
        print(data)  # 'Allen', 'Wang', None, None
        # 'Bob', 'Alice', 'New York City', 'New York'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # setup a question
    ''' create database '''
    # mycursor.execute("CREATE DATABASE combine_two_tables")

    ''' create tables *(execute once)'''
    # mycursor.execute("CREATE TABLE Person(personId INT PRIMARY KEY AUTO_INCREMENT, lastName VARCHAR(50), firstName VARCHAR(50) )")
    # mycursor.execute("CREATE TABLE Address(addressID INT PRIMARY KEY AUTO_INCREMENT, personID INT, city VARCHAR (50), state VARCHAR (50))")

    ''' Insert data row *(execute once)'''
    # persons = (("Wang", "Allen"), ("Alice", "Bob"))
    # mycursor.executemany("INSERT INTO Person(lastName, firstName) VALUES (%s, %s)", persons)
    # db.commit()

    # address = ((2, "New York City", "New York"), (3, "Leetcode", "California"))
    # mycursor.executemany("INSERT INTO Address(personId, city, state) VALUES (%s, %s, %s)", address)
    # db.commit()

    ''' see tables '''
    print("\n+===== Person Table ====+")
    mycursor.execute("SELECT * FROM Person")
    for data in mycursor:
        print(data)

    print("\n+===== Address Table ====+")
    mycursor.execute("SELECT * FROM Address")
    for data in mycursor:
        print(data)

    combineTwoTables()
