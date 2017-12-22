#!/usr/bin/python

# Imports
from flask import Flask, render_template, redirect, url_for, request, session
import os, sys
from app import db

app = Flask(__name__)

HOME_PAGE = 'about.html'

# Home page
@app.route('/')
@app.route('/home')
def home():
    return render_template(HOME_PAGE)

# Login page. Until we have a login page, go to the home page instead.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['Username'])
    return render_template("login.html")

# Sign up page. Until we have a login page, go to the home page instead.
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print(request.form['username'])
        username=request.form['username']
        password=request.form['password']
        password2=request.form['password2']
        if password==password2:
            db.adduser(username, password)
            print("password don't match")
    return render_template("sign_up.html")

@app.route('/Profile', methods=['GET', 'POST'])
def profile():
    return render_template("Profile.html")

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Start the application
if __name__== "__main__":
    db.create_db()
    app.run(debug=True)
