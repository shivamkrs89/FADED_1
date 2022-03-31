import mysql.connector
import bcrypt
from datetime import datetime


def connect():
    try:
        mydb = mysql.connector.connect(
            host='us-cdbr-east-05.cleardb.net',
            user='b70b5b318003ac',
            password='356f8baa',
            database='heroku_af5ccba6c9a4d11',
        )
    except:
        connect()
    return mydb