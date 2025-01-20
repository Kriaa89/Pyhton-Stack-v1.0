import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Email:
    DB = "Email_shcema"
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO validation (email) VALUES (%(email)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM validation;"
        results = connectToMySQL(cls.DB).query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails
    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM  validation WHERE email = %(email)s;"
        data = {
            'email': email
        }
        result = connectToMySQL(cls.DB).query_db(query, data)
        # here we will check the email is already in the database or not 
        if result:
            return cls(result[0])
        return None
    
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM validation WHERE id = %(id)s;"
        data = {
            'id': id
        }

        return connectToMySQL(cls.DB).query_db(query, data)
    
    # this is a static method to validate the email
    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address!")
            is_valid = False
        if Email.get_by_email(email['email']):
            flash("Email already exist!")
            is_valid = False
        return is_valid
        
        