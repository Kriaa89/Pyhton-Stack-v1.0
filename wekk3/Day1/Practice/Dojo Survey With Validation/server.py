# in this file we will import the app from the flask_app folder and run the server from here 
from flask_app import app
# here we will import the users.py file from the controllers folder
from flask_app.controllers import dojos



if __name__ == "__main__":
    app.run(debug=True)