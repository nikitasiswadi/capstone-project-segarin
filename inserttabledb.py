import mysql.connector 

db = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = '',
    database = 'database1'
)

cursor = db.cursor()
query = "INSERT INTO databasee(namafile) VALUES(%s)"
data = [
    ("sawi")
    ]
cursor.executemany(query, data)

db.commit()
print("Data berhasil di insert")
