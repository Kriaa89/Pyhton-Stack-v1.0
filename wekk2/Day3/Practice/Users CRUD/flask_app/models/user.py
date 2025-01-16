from flask_app.config.mysqlconnection import connectToMySQL
class UserCrud:
    DB = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# the get_all method will be used when we need to retrieve all the rows of the table 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        cruds = [] # create an empty list to append our instances of users
        for user in results:
            cruds.append(cls(user))
        return cruds