from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app import EMAIL_REGEX
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app) 


class User:
    def __init__(self, data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.password=data["password"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        
    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO emails (first_name, last_name, email, password created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        results = connectToMySQL("Login_schema").query_db(query, data)
        return results
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL("Login_schema").query_db(query, data)
        if (len(results)==0):
            flash("This email doesn't exis")
            return None
        else:
            return cls(results[0])
    @staticmethod
    def valid_registration(data):
        is_valid = True
        if len(data['first_name']) < 2:
            is_valid =False
            flash("First name must be at least 2 characters.")
        if len(data['last_name']) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters.")
        if len(data['password']) < 8:
            is_valid = False
            flash("The password should be at least 8 characters long")
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash("The password and password confirmation should be the same")
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Please insert a valid email address")
        if User.get_by_email(data['email']):
            is_valid = False
            flash("Email already in use")
        return is_valid
            