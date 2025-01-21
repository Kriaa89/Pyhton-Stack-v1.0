from flask import Flask, render_template, session, redirect, request, flash
from flask_app import  app
from flask_app.models.login_registration import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")

# -----------registration form ---------------
@app.route('/register', methods=['POST'])
def register():
    if not User.valid_registration(request.form):
        return redirect('/')
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    user_id = User.create_one(data)
    session['user_id'] = user_id
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    data = {
        "email": request.form['email'],
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/success')

@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("success.html")


# logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
