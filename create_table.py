# Python implementation to create a table in MySQL
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

# create statement for tblemployee
employeetbl_create = """CREATE TABLE `employee_db`.`tblemployee` (
`empid` INT NOT NULL AUTO_INCREMENT,
`empname` VARCHAR(45) NULL,
`department` VARCHAR(45) NULL,
`salary` INT NULL,
PRIMARY KEY (`empid`))"""

c.execute(employeetbl_create)

c = db.cursor()

# fetch tblemployee details in the database
c.execute("desc tblemployee")

# print the table details
for i in c:
    print(i)

# finally closing the database connection
db.close()
