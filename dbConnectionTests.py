import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Patrycja",
  password="Scully1!",
  database="mydatabase"
)

print(mydb)

mycursor = mydb.cursor()
# # mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("CREATE TABLE players (name VARCHAR(255), address VARCHAR(255))")
# or --> mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("ALTER TABLE players ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
