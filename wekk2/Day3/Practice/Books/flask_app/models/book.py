from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
class Book:
    DB = 'books_shcema'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []
        
    