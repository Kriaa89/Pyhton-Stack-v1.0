from flask import render_template,session,redirect,request
from flask_app import  app
from flask_app.models.login_registration import User

@app.route('/')
def index():
    return render_template("index.html")

# -----------registration form ---------------
@app.route('/register', methods=['POST'])
def register():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
    }
    if User.valid_registration(data)==False:
        return render_template("index.html", data=data)
    else:
        data['password']=User.encrypt_string(data['password'])
        results=User.create_one(data)
        session['user_id']=results
        return redirect('/success')
    
@app.route('/success', methods=['POST'])
def login():
    data = {
        "email": request.form['email'],
    }
    user_in_db = User.get_by_email(data)
    # here we are cheking if the user is in the database
    if user_in_db==None:
        return render_template("index.html", data1=data)
    else:
        # here we are checking if the password is correct
        if not User.validate_password(request.form['password'], user_in_db.password):
            return render_template("index.html", data1=data)
        else:
            # here we are storing the user id in the session
            session['user_id']=user_in_db.id
            #  here we are storing the user first name in the session
            session['first_name']=user_in_db.first_name
            # # here we are storing the user last name in the session
            session['last_name']=user_in_db.last_name
            return redirect('/success')