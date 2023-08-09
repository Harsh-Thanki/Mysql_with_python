# Python implementation to insert data into a table in MySQL
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

# insert statement for tblemployee
# this statement will enable us to insert multiple rows at once.
employeetbl_insert = """INSERT INTO tblemployee (
empname,
department,
salary)
VALUES (%s, %s, %s)"""

# we save all the row data to be inserted in a data variable
data = [("Vani", "HR", "100000"),
        ("Krish", "Accounts", "60000"),
        ("Aishwarya", "Sales", "25000"),
        ("Govind", "Marketing", "40000")]

# execute the insert commands for all rows and commit to the database
c.executemany(employeetbl_insert, data)
db.commit()

# finally closing the database connection
db.close()
