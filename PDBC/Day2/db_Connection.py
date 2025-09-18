import mysql.connector

def db_Connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="HDFCBank"
    )
print("db connected successfully.....")    