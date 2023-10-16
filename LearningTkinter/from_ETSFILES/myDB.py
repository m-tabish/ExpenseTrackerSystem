import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user ="root" ,
    password = "tabish111",
    database = 'db1'
    )

cur = mydb.cursor()
# s = "CREATE TABLE book(bookid integer(4), title varchar(20), price float(5,2) )"

# books  = [[1, "HARRY POTTER -1", 500],
#           [2, "ATOMIC HABITS", 600]]
# # s = "INSERT INTO book (bookid, title , price)  VALUES (%s,%s,%s)"
# data = list(zip(books))
# print(data)
# cur.executemany(s,books)

s= "SELECT * FROM book;"

cur.execute(s)
data = cur.fetchall()
for i in data:
    print (i)
    
    
mydb.commit()
cur.close()
mydb.close()
mydb.disconnect()