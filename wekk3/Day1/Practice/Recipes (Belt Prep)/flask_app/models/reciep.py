from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# explination of this file 
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
        self.user = ""  # here we will store the user's full name when we get the recipe with the user

    @classmethod
    def get_all_with_users(cls):
        # this query will give us all creator full names with the recipe data
        query = """
            SELECT recipes.*, users.first_name, users.last_name 
            FROM recipes 
            JOIN users ON recipes.user_id = users.id;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        all_recipes = [] # here will store all the instance of recipes
        for row in results: 
            recipe = cls(row)
            recipe.user = f"{row['first_name']} {row['last_name']}" # here we are storing the full name of the user 
            all_recipes.append(recipe)  # here we are storing the instance of the recipe in the list 
        return all_recipes 

    @classmethod
    def save(cls, data):
        # this query will insert the recipe data into the database
        query = """
            INSERT INTO recipes (name, description, instruction, under_30, 
            cook_date, user_id, created_at, updated_at) 
            VALUES (%(name)s, %(description)s, %(instruction)s, %(under_30)s, 
            %(cook_date)s, %(user_id)s, NOW(), NOW());
        """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_one(cls, data):
        # this query will get the recipe data by id and we gonna use this method to get the recipe data by id
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        # this query will update the recipe data by id 
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instruction=%(instruction)s, under_30=%(under_30)s, cook_date=%(cook_date)s WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        # this query will get all the recipes data and we gonna use this method to get all recipes data 
        query = """
        SELECT recipes.*, users.first_name, users.last_name, recipes.user_id
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
    
    @classmethod
    def get_one_with_user(cls, data):
        # this query will get the recipe data by id and we use this method in the show recipe route to get who created the recipe
        query = """
            SELECT recipes.*, users.first_name, users.last_name 
            FROM recipes 
            JOIN users ON recipes.user_id = users.id 
            WHERE recipes.id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        if results:
            row = results[0]
            recipe = cls(row)
            recipe.user = f"{row['first_name']} {row['last_name']}"
            return recipe
        return None
    
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