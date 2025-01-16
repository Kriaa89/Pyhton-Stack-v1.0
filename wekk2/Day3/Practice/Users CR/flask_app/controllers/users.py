from  flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

# this route will display all the users from the database
@app.route('/')
def index():
    all_users=User.get_all()
    return render_template('index.html', users=all_users)

# this route will display the form to create a new user
@app.route('/user/create', methods=['GET'])
def create():
    return render_template('create.html')

# this route will create a new user
@app.route('/create', methods=['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/')