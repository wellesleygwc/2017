#!/usr/bin/python

# Imports
from flask import Flask, flash, render_template, redirect, url_for, request, session
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

# Help page
@app.route('/help', methods=['GET', 'POST'])
def help():
    return render_template('Help.html')


#contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('Contacts.html')

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
        role=request.form['role']
        adminPass = request.form['adminPass']
        EventCPass = request.form['EventCPass']


        print (role)
        if role=="Administrator":
            if adminPass == "TQW5Y":
                print ("success on admin Pass")
            else:
                error = "The administrator code is incorrect please try again or ask your administrator for the code."
                return render_template("sign_up.html", error=error)


        if role =="EventC":
                if EventCPass== "LSVY6":
                    print ("success on EventCPass")
                else:
                    error = "The event coordinator code is incorrect please try again or ask your administrator for the code."
                    return render_template("sign_up.html", error=error)



        if password==password2:
            if db.userexists(username):
                error="Username already in use"
            else:
                db.adduser(username, role, password, firstname, lastname, email, phone)
                flash('You have successfully created an account!')
                return render_template("login.html")
        else:
            error="The passwords do not match"

    return render_template("sign_up.html", error=error)


@app.route('/Profile', methods=['GET', 'POST'])
def profile():
    if not 'username' in session:
        print ("no session")
        return render_template('login.html')
    user=db.getprofile(session ['username'])
    print (user)
    return render_template('Profile.html', user=user)

@app.route('/EditProfile', methods=['GET', 'POST'])
def editprofile():
    if not 'username' in session:
        print ("no session")
        return render_template('Login.html')
    if request.method == 'GET':
        user=db.getprofile(session ['username'])
        return render_template('EditProfile.html')

    old_password = request.form['old_password']
    new_password=request.form['new_password']
    confirm_password=request.form['confirm_password']
    username = session['username']
    print (' username:%s, new_password:%s, confirm_password:%s' % (username, new_password, confirm_password))
    if new_password!=confirm_password:
        return render_template('Profile.html', error_message="passwords don't match")
    username=session['username']
    status = db.change_password(username, old_password, new_password)
    user=db.getprofile(session ['username'])
    return render_template('Profile.html', error_message=status,user=user)

    new_email = request.form['new_email']
    new_first_name = request.form['new_first_name']
    new_last_name = request.form['new_last_name']
    print (' username:%s, new_email:%s, new_first_name:%s, new_last_name:%s' % (username, new_email, new_first_name, new_last_name))

    return render_template('login.html', error_message=status)

#
# Delete a user account
#
@app.route('/deleteaccount')
def deleteaccount ():
    del session['username']
    return redirect(url_for('home'))

# Log out when hit log out button
@app.route('/logout')
def logout():
    del session['username']
    return redirect(url_for('home'))

# Events page
@app.route('/events')
def events():
    return render_template('Events.html', events=db.list_events())

@app.route('/volunteer', methods=['GET','POST'])
def volunteer():
    if request.method == "GET":
        event_id = int(request.args.get('id'))
        events = db.list_events()
        event = events[event_id - 1]
        signups = db.list_signups(event_id)
        return render_template('Volunteer.html', id=request.args.get('id'), event=event, signups=signups)

    db.volunteer(request.form['id'], session['username'])
    return redirect(url_for('events'))

# add event
@app.route('/addevent', methods=['GET','POST'])
def addevent():
    if request.method == "GET":
        return render_template('AddEvent.html')
    if request.method == "POST":

        print(request.form['Title'])
        print(request.form['Description'])
        print(request.form['NumberOfVolunteers'])
        print(request.form['Date'])
        print(request.form['Time'])
        print(session['username'])

        Title = request.form['Title']
        Description= request.form['Description']
        NumberOfVolunteers= 0
        try:
            NumberOfVolunteers = int(request.form['NumberOfVolunteers'])
            print (request.form ['NumberOfVolunteers'])
        except ValueError:
            flash ('Please enter a valid number of volunteers')
            print (request.form ['please enter a valid number of volunteers'])
            return render_template('AddEvent.html')

        Date = request.form['Date']
        Time = request.form['Time']
        NumberOfCredits = 0
        try:
             NumberOfCredits = int(request.form['NumberOfCredits'])
             print (request.form ['NumberOfCredits'])
        except ValueError:
            flash ('Please enter a valid number of credits')
            print (['please enter a valid number of credits'])
            return render_template('AddEvent.html')
        NumberOfCredits= request.form['NumberOfCredits']

        print("'%s'" % NumberOfCredits)
        flash('You have successfully created an event!')
        db.add_event(Title, Description, Date, NumberOfCredits, NumberOfVolunteers, session['username'])
        return redirect(url_for('events'))



# Start the application
if __name__== "__main__":
    db.create_db()
    app.secret_key = os.urandom(24)
    app.run(debug=True)

# menu
@app.route('/menu')
def menu():
    return render_template('menu.html')

