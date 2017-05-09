#!C:\Python34\python.exe
print("Content-Type: text/html\r\n\r\n")
print("Hello Python")
import sqlite3
conn=sqlite3.connect('project.db')
cursor=conn.execute("select * from USERS;")
cursor=cursor.fetchall()
for row in cursor:
     print(row[0])
     print(row[1])
     print(row[2])
     print(row[3])
     print(row[4])



