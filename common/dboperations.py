import mysql.connector
import bcrypt
from datetime import datetime
from common import connect
from business_logic import codechef,codeforces

def insert_ratings_codeforces(user_id,handle: str):
    mydb = connect.connect()
    mycursor = mydb.cursor()
    user_data = codeforces.codeForces(handle)
    try:
        insertFn = "INSERT INTO codforces_data (uid,ratings,no_qns,no_contests,max_ratings,user_handle) VALUES (%s,%s,%s,%s,%s,%s) "
        registration_info = (user_id,user_data[0], user_data[1], user_data[2], user_data[3], handle)
        mycursor.execute(insertFn, registration_info)
        mydb.commit()
        return 1
    except:
        mycursor.execute(
            "UPDATE codforces_data  SET ratings=%s,no_qns=%s,no_contests=%s,max_ratings=%s,user_handle=%s  where uid=%s""",
            (user_data[0], user_data[1], user_data[2], user_data[3], handle, user_id))
        mydb.commit()
        return 1


def insert_ratings_codechef(user_id, handle: str):
    mydb = connect.connect()
    mycursor = mydb.cursor()
    user_data = codechef.codeChef(handle)
    try:
        insertFn = "INSERT INTO codechef_data (uid,ratings,no_qns,partially_solved,no_contests,user_handle) VALUES (%s,%s,%s,%s,%s,%s) "
        registration_info = (user_id, user_data[0], user_data[1], user_data[2], user_data[3], handle)
        mycursor.execute(insertFn, registration_info)
        mydb.commit()

        return 1
    except:
        mycursor.execute(
            "UPDATE codechef_data  SET ratings=%s,no_qns=%s,partially_solved=%s,no_contests=%s,user_handle=%s  where uid=%s",
            (user_data[0], user_data[1], user_data[2], user_data[3], handle, user_id))
        mydb.commit()
        return 1

def getLeaderboard():
    mydb = connect.connect()
    mycursor = mydb.cursor()

    statement= "SELECT * from codechef_data"
    mycursor.execute(statement)
    fetched_list = mycursor.fetchall()

    return fetched_list
def getLeaderboard1():
    mydb = connect.connect()
    mycursor = mydb.cursor()

    statement= "SELECT * from codforces_data"
    mycursor.execute(statement)
    fetched_list = mycursor.fetchall()

    return fetched_list

def getVotes(userId):
    mydb = connect.connect()
    mycursor = mydb.cursor()
    statement = "SELECT no_upvotes,no_downvotes from users where id=%s"
    mycursor.execute(statement, (userId))
    fetched_list = mycursor.fetchall()

    return fetched_list





