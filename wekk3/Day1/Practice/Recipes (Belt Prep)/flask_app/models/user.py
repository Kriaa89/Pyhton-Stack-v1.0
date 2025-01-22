from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import EMAIL_REGEX, bcrypt
class User:
    DB = 'reciepie_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users(first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data["firt_name"]) < 2:
            is_valid = False
            flash("First name must be at least 2 characters.")
        if len(data["last_name"]) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters.")
        if not EMAIL_REGEX.match(data["email"]):
            flash("invalid email address.")
            is_valid = False
        if User.get_by_email({"email": data['email']}):
            flash("Email already in use.")
            is_valid = False
        if len(data["password"]) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Passwords do not match.")
            is_valid = False
        return is_valid