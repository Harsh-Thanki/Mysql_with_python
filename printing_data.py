# Python implementation to fetch data from a table in MySQL
import mysql.connector

# connecting to the mysql server

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="employee_db"
)

# cursor object c
c = db.cursor()

# select statement for tblemployee which returns all columns
employeetbl_select = """SELECT * FROM tblemployee"""

# execute the select query to fetch all rows
c.execute(employeetbl_select)

# fetch all the data returned by the database
employee_data = c.fetchall()

# print all the data returned by the database
for e in employee_data:
    print(e)

# finally closing the database connection
db.close()
