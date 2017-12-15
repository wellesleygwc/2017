#!/usr/bin/python

# Imports
from flask import Flask, render_template, redirect, url_for, request, session
import os, sys
from app import db

app = Flask(__name__)

HOME_PAGE = 'Events.html'

# Home page
@app.route('/')
@app.route('/home')
def home():
    return render_template(HOME_PAGE, events=db.list_events())

# Login page. Until we have a login page, go to the home page instead.
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template(HOME_PAGE)

# Start the application
if __name__== "__main__":
    db.create_db()
    app.run(debug=True)
