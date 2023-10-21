import mysql.connector

attendence = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tabish111",  # Replace with your MySQL password
    database="attendence"  # Specify the database you want to use
)

cur = attendence.cursor()

# Define the SQL statement for creating a table
# s = "CREATE TABLE record (serial_no INT(11), name VARCHAR(50), entry INT(11), `exit` INT(11));"
# s = "INSERT INTO record (serial_no, name, entry, `exit`) VALUES (%s,%s,%s,%s);"
# db1 = (1, "Tabish ", 23, 13)
s = "select * from record;"
# Execute the SQL statement
cur.execute(s)

# Commit the changes and close the connection
attendence.commit()
attendence.close()
