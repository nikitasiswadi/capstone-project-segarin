import mysql.connector 

db = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = '',
    database = 'database1'
)

cursor = db.cursor()
query = "INSERT INTO login(username, email, password) VALUES(%s, %s, %s)"
data = [
    ("aqoehsyantik", "aqoehsyantiksyalala@gmail.com", ""),
    ("kamoehsyantik", "kamoehsyantiksyalala@gmail.com", "kiwkiwkiw")
]

cursor.executemany(query, data)
db.commit()

print("Data berhasil di insert")