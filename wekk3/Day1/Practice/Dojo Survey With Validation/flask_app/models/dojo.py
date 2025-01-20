from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Dojo:
    DB = 'dojo_survey_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at =data['created_at']
        self.updated_at =data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) < 3:
            flash("you must enter a location.")
            is_valid = False
        if len(dojo['language']) < 3:
            flash("you must enter a language.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("comment must be at leat 3 characters.")
            is_valid = False
        return is_valid