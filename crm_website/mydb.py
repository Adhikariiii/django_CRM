import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'pa@2003kapan'

)

cursor = database.cursor()
cursor.execute('CREATE DATABASE older')

print('all good')