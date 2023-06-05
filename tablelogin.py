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
    CREATE TABLE Login(
    id_user INT AUTO_INCREMENT PRIMARY KEY, 
    username VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL,
    password VARCHAR(150) NOT NULL
    )
    """
)

print("Yeay table berhasil dibuat")