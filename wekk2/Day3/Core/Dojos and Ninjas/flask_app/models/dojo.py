from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
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
# we need to create get_dojo_with_ninjas class method to get all the ninjas that belong to a specific doho
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        # results will be a list of topping objects with the burger attached to each row
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                "id": row['ninjas.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "dojo_id": row['dojo_id'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_data))
            return dojo