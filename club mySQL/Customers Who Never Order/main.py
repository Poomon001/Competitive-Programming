import os
import mysql.connector
from dotenv import load_dotenv

# Setup database
load_dotenv()
db = mysql.connector.connect(host=os.getenv("HOST"), user=os.getenv("USER"), passwd=os.getenv("PASSWD"),
                                 database=os.getenv("DATABASE"))

mycursor = db.cursor()

'''
    Link: https://leetcode.com/problems/customers-who-never-order/
    Purpose: Find a customer who never ordered from mySQL database in any order
    parameter: none
    return: none
    Pre-Condition: none
    Post-Condition: none
'''
def customersWhoNeverOrder():
    print("\n+===== Answer =====+")
    mycursor.execute("SELECT name AS Customers FROM Customers WHERE id NOT IN (SELECT customerId FROM Orders)")
    for data in mycursor:
        print(data) # Henry, Max

if __name__ == '__main__':
    # setup a question
    ''' create database '''
    # mycursor.execute("CREATE DATABASE customers_who_never_order")

    ''' create tables *(execute once)'''
    # mycursor.execute("CREATE TABLE Customers( name VARCHAR (50), id int PRIMARY KEY AUTO_INCREMENT)")
    # mycursor.execute("CREATE TABLE Orders( customerId int, id int PRIMARY KEY AUTO_INCREMENT)")

    ''' Insert data row *(execute once)'''
    # customers = (("Joe",), ("Henry",), ("Sam",), ("Max",))
    # mycursor.executemany("INSERT INTO Customers(name) VALUES (%s)", customers)
    # db.commit()

    # orders = ((3,), (1,))
    # mycursor.executemany("INSERT INTO Orders(customerId) VALUES (%s)", orders)
    # db.commit()

    ''' see tables '''
    print("\n+===== Customers Table ====+")
    mycursor.execute("SELECT * FROM Customers")
    for data in mycursor:
        print(data)

    print("\n+===== Orders Table ====+")
    mycursor.execute("SELECT * FROM Orders")
    for data in mycursor:
        print(data)

    customersWhoNeverOrder()


