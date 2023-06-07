import pymysql
from random import randint

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="test"

)
mycursor = mydb.cursor()

mycursor.execute("select * from pengguna")
myresult = mycursor.fetchall()
print(len(myresult))
print(True)
test = randint(100,999)
print(test)
