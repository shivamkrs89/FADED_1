import os, sys
from flask import Flask, request, session, render_template, flash, redirect, url_for
from common import dblogin, dboperations
import operator

from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='template/')
app.secret_key = 'the random string'

# def sortByScore():
#     details = pd.DataFrame(students, columns=['Name', 'Age',
#                                               'Place', 'College'],
#                            index=['b', 'c', 'a', 'e', 'f',
#                                   'g', 'i', 'j', 'k', 'd'])
#
#     # Sort the rows of dataframe by 'Name' column
#     rslt_df = details.sort_values(by='Name')
#
#     # show the resultant Dataframe
#     rslt_df
#


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/signup', methods=["POST", "GET"])
def signup():
    if session.get('user_logged_in'):
        return redirect(url_for('dashboard'))
    else:
        if request.method == "POST":
            form_data = request.form.to_dict()
            fname = form_data['fname']
            passwd = form_data['pass']
            email = form_data['email']
            passwdchk = form_data['passcheck']

            if passwd != passwdchk:
                flash("Password doesn't match!")
                render_template('signup.html')

            success = dblogin.user_registration(fname, email, passwd)
            print(str(success))
            if success == 0:
                flash("email already exists, please login")
                return render_template('signup.html')
            elif success == 1:
                print("success")
                return redirect(url_for('login'))

        return render_template('signup.html')


@app.route('/dashboard', methods=["POST", "GET"])
def dashboard():
    if session.get('user_logged_in'):
        if request.method == "POST":
            form_data = request.form.to_dict()
            handle_cf = form_data['cf_handle']
            handle_cc = form_data['cc_handle']
            if handle_cf != "":
                print(dboperations.insert_ratings_codeforces(session['user_id'], handle_cf))
            if handle_cc != "":
                print(dboperations.insert_ratings_codechef(session['user_id'], handle_cc))
            return redirect(url_for('dashboard'))
        return render_template('dashboard.html')
    return redirect(url_for('login'))


@app.route('/login', methods=["POST", "GET"])
def login():
    if session.get('user_logged_in'):
        return redirect(url_for('dashboard'))
    else:
        if request.method == "POST":
            form_data = request.form.to_dict()
            passwd = form_data['pass']
            email = form_data['email']
            success = dblogin.user_login(email, passwd)
            print(success)
            if success[0][0] == 0:
                flash("Wrong credentials")
                return render_template('login.html')
            elif success[0][0] == 1:
                print("success")
                session['user_id'] = success[0][0]
                session['user_logged_in'] = True
                print(session['user_id'])
                return redirect(url_for('dashboard'))

        return render_template('login.html')


@app.route('/leaderboard', methods=["POST", "GET"])
def leaderboard():
    if session.get('user_logged_in'):
        print("here")

        list1 = dboperations.getLeaderboard()
        list2 = dboperations.getLeaderboard1()
        userid = session['user_id']

        score_dict = getDict(list1, list2)
        sorted(score_dict, key=score_dict.get)
        sorted_dict = dict(sorted(score_dict.items(),
                                  key=operator.itemgetter(1),
                                  reverse=True))
        print(sorted_dict)

        return render_template('leaderboard.html', list=list1,list2=list2,dict1=sorted_dict, len=len(list1),len2=len(list2),len3=len(sorted_dict))

    return redirect(url_for('login'))



def getDict(list,list2):
    dict={}

    for x in list:
        score = 0
        score += (x[1]* (1.5) +x[2]*30 + x[3]*70)
        key = x[0]

        if key not in dict:
            dict[key] = score
        else:
            dict[key] = dict[key] + score

    for x in list2:
        score = 0
        score+=(x[1]*(1.5)+x[3]*70)
        key = x[0]

        if key not in dict:
            dict[key] = score
        else:
            dict[key]=dict[key]+score
    return dict



if __name__ == "__main__":
    app.run(debug="true")
