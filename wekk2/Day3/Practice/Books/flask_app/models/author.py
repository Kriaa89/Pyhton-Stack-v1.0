# this file will containe the query for the author table and the class AuthorCrud we gonna use to intercat with database and 
# and we gonna import this method in the controller file 
# the methods we need to implement are:
from flask_app.config.mysqlconnection import connectToMySQL
class Author:
    DB = 'books_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # we need to have a list in case we want to show books related to the author
    
    # this method will save the author in the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_author_books(cls, data):
        # this query will give us 
        query = "SELECT * FROM authors JOIN books ON authors.id = books.author_id WHERE authors.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        author = cls(results[0])
        for row in results:
            # now we need to parse author data to make instance of the authors and add them to the list.
            books_data = {
                'id': row['books.id'],
                'title': row['title'],
                'num_of_pages': row['num_of_pages'],
                'created_at': row['books.created_at'],
                'updated_at': row['books.updated_at'],
            }
            author.