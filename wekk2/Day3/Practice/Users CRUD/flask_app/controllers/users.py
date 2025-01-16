from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.user import UserCrud

# this route will display all the users from the database 
@app.route('/')
def index():
    all_cruds = UserCrud.get_all()
    return render_template('index.html', cruds=all_cruds)

# this route will display the form to create a new user
@app.route('/users/new', methods=['GET'])
def new_user():
    return render_template('add_user.html')