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

# this route will create a new user
@app.route('/users/create', methods=['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    UserCrud.save(data)
    return redirect('/')

# this route will allow us to edit the data of the user 
@app.route('/users/edit/<int:id>', methods=['GET'])
def edit_user():
    UserCrud.update(request.form)
    return redirect('/')