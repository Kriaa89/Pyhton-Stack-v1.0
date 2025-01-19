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
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books(title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.DB).query_db(query)
        books = []
        for row in results:
            books.append(cls(row))
        return books
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    
    @classmethod
    def add_favorite_athor(cls, data):
        query = "INSERT INTO favorits (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    
    @classmethod
    def get_favorites_authors(cls, data):
        query = """
        SELECT * FROM auhtors
        LEFT JOIN favorites ON author.id = favorites.author_id
        WHERE favorites.book_id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        book = cls(results[0])
        for row in results:
            author_data = {
                'id': row['authors.id'],
                'name': row['name'],
                'created_at': row['authors.created_at'],
                'updated_at': row['authors.updated_at'],
            }
            book.authors.append( author.Author(author_data))
            return book