from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
class Dojo:
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # we create an empty list to store in all the ninjas that belong to a specific dojo
        self.ninjas = [] 
# we need to create a class method save the dojo to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOw(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)
# we need to create a class method to get all the dojos from the database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
# we need to loop over the results to create instances of the Dojo class and append them to the dojos list
        for dojo in results:
            dojos.append(cls(dojo))
            return dojos
    # 