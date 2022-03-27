import mysql.connector
import bcrypt
from datetime import datetime


def connect():
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='shivam@123',
            database='codemate',
        )
    except:
        connect()
    return mydb