from flask_app.config.mysqlconnection import connectToMySQL
class User:
    DB = 'users_schema'
    def __init__(self, data):
        self.id =data['id']
        self.first_name =data['first_name']
        self.last_name =data['last_name']
        self.email =data['email']
        self.created_at =data['created_at']
        self.updated_at =data['updated_at']
    
    # this method will save the user to the database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append( cls(user))
        return users
    # the get one method will be used to get a single user from the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users(first_name, last_name, email, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('users_schema').query_db( query, data )