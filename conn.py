# Python implementation to create a Database in MySQL
import mysql.connector

# connecting to the mysql server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password"
)

# cursor object c
c = db.cursor()

# executing the database creation statement
c.execute("CREATE DATABASE employee_db")

# fetching all the databases
c.execute("SHOW DATABASES")

# printing all the databases
for i in c:
    print(i)
c = db.cursor()

# finally closing the database connection
db.close()
