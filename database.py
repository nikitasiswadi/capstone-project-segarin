import mysql.connector 

db = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = '',
    database = 'database1'
)

cursor = db.cursor()
cursor.execute(
    """
    CREATE TABLE databasee(
    id_user INT AUTO_INCREMENT PRIMARY KEY, 
    namafile VARCHAR(100) NOT NULL
    )
    """
)

print("Yeay table berhasil dibuat")