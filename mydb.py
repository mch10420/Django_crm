import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'MichaelEDudgeonIII'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print('All done!')