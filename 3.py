#!C:\Python34\python.exe
print("Content-Type: text/html\r\n\r\n")
import sqlite3,cgi,cgitb
form=cgi.FieldStorage()
a=form.getvalue("fname")
b=form.getvalue("lname")
c=form.getvalue("uname")
d=form.getvalue("pwd")
e=form.getvalue("Email")
conn=sqlite3.connect('project.db')
cursor=conn.execute("insert into USERS (Firstname,Lastname,Username,Password,Email) values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"');")
conn.commit()
print("<html>")
print("<head>")
print("</head>")
print("Registration Succesfully.")
conn.close()



