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
        query = "INSERT INTO validations (email) VALUES (%(email)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM validations;"
        results = connectToMySQL(cls.DB).query_db(query)
        emails = []
        for emails in results:
            emails.append(cls(email))
        return emails
    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid
        
        