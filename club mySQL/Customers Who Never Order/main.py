import mysql.connector

if __name__ == '__main__':
    db = mysql.connector.connect(host="...", user="...", passwd="...", database="database_that_will_be_used")