from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    DB = 'reciepie_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under_30 = data['under_30']
        self.cook_date = data['cook_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None  # Will store user info when needed

    @classmethod
    def get_all_with_users(cls):
        query = """
            SELECT recipes.*, users.first_name, users.last_name 
            FROM recipes 
            JOIN users ON recipes.user_id = users.id;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        all_recipes = []
        for row in results:
            recipe = cls(row)
            recipe.user = f"{row['first_name']} {row['last_name']}"
            all_recipes.append(recipe)
        return all_recipes

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO recipes (name, description, instruction, under_30, 
            cook_date, user_id, created_at, updated_at) 
            VALUES (%(name)s, %(description)s, %(instruction)s, %(under_30)s, 
            %(cook_date)s, %(user_id)s, NOW(), NOW());
        """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instruction=%(instruction)s, under_30=%(under_30)s, cook_date=%(cook_date)s WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = """
        SELECT recipes.*, users.first_name, users.last_name 
        FROM recipes 
        JOIN users ON recipes.user_id = users.id;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        recipes = []
        for row in results:
            recipe = cls(row)
            recipe.user = f"{row['first_name']} {row['last_name']}"
            recipes.append(recipe)
        return recipes
    
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at least 3 characters")
            is_valid = False
        if len(data['instruction']) < 3:
            flash("Instructions must be at least 3 characters")
            is_valid = False
        if 'under_30' not in data:
            flash("Under 30 minutes field is required")
            is_valid = False
        if not data['cook_date']:
            flash("Date cooked is required")
            is_valid = False
        return is_valid