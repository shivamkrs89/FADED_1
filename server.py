import os, sys
from flask import Flask, request, session, render_template, flash, redirect, url_for
from common import dblogin, dboperations
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='template/')
app.secret_key = 'the random string'


@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        form_data = request.form.to_dict()
        fname = form_data['fname']
        passwd = form_data['pass']
        email = form_data['email']
        passwdchk = form_data['passcheck']

        if passwd != passwdchk:
            flash("Password doesn't match!")
            render_template('signup.html')



        success = dblogin.user_registration(fname,email, passwd)
        print(str(success))
        if success == 0:
            flash("email already exists, please login")
            return render_template('signup.html')
        elif success == 1:
            print("success")
            return redirect(url_for('signup'))

    return render_template('signup.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        form_data = request.form.to_dict()
        passwd = form_data['pass']
        email = form_data['email']
        success = dblogin.user_login(email, passwd)
        print(str(success))
        if success == 0:
            flash("Wrong credentials")
            return render_template('login.html')
        elif success == 1:
            print("success")
            return redirect(url_for('#'))

    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug="true")



