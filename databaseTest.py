import mysql.connector

conn = mysql.connector.connect(username='root', password='Aditya@123',host='localhost',database='face_recognizer1',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()