import mysql.connector
import bcrypt
from datetime import datetime
from common import connect


def user_registration(fname: str, email: str, passwd: str):
    mydb = connect.connect()
    mycursor = mydb.cursor()
    hassedPasswd = bcrypt.hashpw(passwd.encode("utf-8"), bcrypt.gensalt())
    try:
        insertFn = "INSERT INTO users (name,email,pwd) VALUES (%s, %s, %s)"
        registration_info = (fname, email, hassedPasswd)
        mycursor.execute(insertFn, registration_info)
        mydb.commit()
        return 1
    except:
        return 0  # email exists

def user_login(emailid: str, passwd: str):
    mydb = connect.connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT pwd from users where email = \"" + emailid + "\"")
    fetched_list = mycursor.fetchall()
    if (len(fetched_list) == 0):
        print("user not found")
        fetched_list=[('2')]
        return fetched_list  # email id not found

    else:
        hassedPasswd = fetched_list[0][0]
        print(hassedPasswd.encode("utf-8"),passwd.encode("utf-8"))
        if bcrypt.checkpw(passwd.encode("utf-8"), hassedPasswd.encode("utf-8")):
            mycursor.execute("SELECT name,email,overall_score,no_upvotes,no_downvotes from users where email = \"" + emailid + "\"")
            fetched_list = mycursor.fetchall()

            return fetched_list
        else:
            print("incorrect pwd")
            fetched_list = [('0')]
            return fetched_list  # incorrect password

print(user_login("ab@a.com","b"))