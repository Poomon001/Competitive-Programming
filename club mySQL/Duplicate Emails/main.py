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
def duplicateEmail():
    print("\n+===== Answer =====+")
    mycursor.execute("SELECT email FROM Person GROUP BY email HAVING count(email) > 1") # 'a@b.com', 'y@z.com'
    for data in mycursor:
        print(data)

if __name__ == '__main__':
    # setup a question
    ''' create database '''
    # mycursor.execute("CREATE DATABASE duplicate_emails")
    mycursor.execute("USE duplicate_emails")

    ''' create tables *(execute once)'''
    # mycursor.execute("CREATE TABLE Person( email VARCHAR (50), id int PRIMARY KEY AUTO_INCREMENT)")
    # mycursor.execute("CREATE TABLE Orders( customerId int, id int PRIMARY KEY AUTO_INCREMENT)")

    ''' Insert data row *(execute once)'''
    # person = (("a@b.com",), ("c@d.com",), ("y@z.com",), ("a@b.com",), ("y@z.com",), ("y@z.com",),)
    # mycursor.executemany("INSERT INTO Person(email) VALUES (%s)", person)
    # db.commit()

    ''' see tables '''
    '''
    ('a@b.com', 1)
    ('c@d.com', 2)
    ('y@z.com', 3)
    ('a@b.com', 4)
    ('y@z.com', 5)
    ('y@z.com', 6)
    '''
    # print("\n+==== Person Table ====+")
    # mycursor.execute("SELECT * FROM Person")
    # for data in mycursor:
    #     print(data)

    duplicateEmail()


