import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Mydatabase@99#"
)
mycursor = connection.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)

    

