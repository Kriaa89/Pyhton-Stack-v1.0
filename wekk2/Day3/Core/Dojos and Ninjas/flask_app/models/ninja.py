from flask_app.config.mysqlconnection import connectToMySQL
class Ninja:
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id'],
        self.first_name = data['name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        