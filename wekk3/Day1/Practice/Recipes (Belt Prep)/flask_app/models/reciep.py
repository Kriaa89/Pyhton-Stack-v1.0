from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Recipe:
    DB = 'reciepie_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.user_id = data['user_id']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, data):
        query = """INSERT INTO recipes (name, user_id, description, instruction, under_30, created_at, updated_at) 
        VALUES (%(name)s, %(user_id)s, %(description)s, %(instruction)s, %(under_30)s, NOW(), NOW());"""
        return connectToMySQL(cls.DB).query_db(query, data)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.DB).query_db(query)
        recipes = []
        for row in results:
            recipes.append(cls(row))
        return recipes
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, desciption = %(desciption)s, instruction = %(instruction)s, under_30 = %(under_30)s, updated_at = NOW() created_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(data['description']) < 3:
            is_valid = False
            flash("description must be at least 3 characters.")
        if len(data['instruction']) < 3:
            is_valid = False
            flash("instruction must be at least 3 characters.")
        return is_valid