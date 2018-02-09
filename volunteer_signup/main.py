#!/usr/bin/python

# Imports
from flask import Flask, render_template, redirect, url_for, request, session
import os, sys
from app import db

app = Flask(__name__)

HOME_PAGE = 'index.html'

# Home page
@app.route('/')
@app.route('/home')
def home():
    return render_template(HOME_PAGE)

# Home page
@app.route('/about')
def about():
    return render_template('about.html')

# Login page. Until we have a login page, go to the home page instead.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['Username'])
        print(request.form['Password'])
        username = request.form['Username']
        password = request.form['Password']

        error = db.checkuser(username, password)
        if error == "Congratulations":

            session['username'] = username

            return redirect(url_for('events'))
        else:
            return render_template("login.html", error=error, loggedin='username' in session)


    return render_template("login.html")

# Sign up page. Until we have a login page, go to the home page instead.
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        print(request.form['username'])
        username=request.form['username']
        password=request.form['password']
        password2=request.form['password2']
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        email=request.form['email']
        phone=request.form['phone']


        if password==password2:
            if db.userexists(username):
                error="Username already in use"
            else:
                db.adduser(username, password, firstname, lastname, email, phone)
        else:
            error="The passwords do not match"

    return render_template("sign_up.html", error=error)

@app.route('/Profile', methods=['GET', 'POST'])
def profile():
    if not 'username' in session:
        print ("no session")
        return render_template('Profile.html')
    if request.method == 'GET':
        return render_template('Profile.html')
    old_password = request.form['old_password']
    new_password=request.form['new_password']
    confirm_password=request.form['confirm_password']
    username = session['username']
    print (' username:%s, new_password:%s, confirm_password:%s' % (username, new_password, confirm_password))
    if new_password!=confirm_password:
        return render_template('Profile.html', error_message="passwords don't match")
    username=session['username']
    status = db.change_password(username, old_password, new_password)

    return render_template('login.html', error_message=status)


# Events page
@app.route('/events')
def events():
    return render_template('Events.html', events=db.list_events())

# menu
@app.route('/addevent')
def addevent():
    return render_template('AddEvent.html')

# Start the application
if __name__== "__main__":
    db.create_db()
    app.secret_key = os.urandom(24)
    app.run(debug=True)

# menu
@app.route('/menu')
def menu():
    return render_template('menu.html')

