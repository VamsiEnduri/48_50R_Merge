# python --> database :-- mysql-python-connector 

import mysql.connector

# print(mysql.connector)

def get_connection():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="EmployeeManagementSystem"
)

print("db connected successfully")