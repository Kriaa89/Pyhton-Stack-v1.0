from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.book import Book
class Author:
    DB = 'books_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []
    
    # this method will save the author in the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.DB).query_db(query)
        authors = []
        for row in results:
            authors.append(cls(row))
        return authors
    
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    
    @classmethod
    def add_favorite_book(cls, data):
        query = "INSERT INTO favorits (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    
    @classmethod
    def get_favorites_books(cls, data):
        query = """
        SELECT * FROM books
        LEFT JOIN favorites ON books.id = favorites.book_id
        WHERE favorites.author_id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        author = cls(results[0])
        for row in results:
            book_data = {
                'id': row['books.id'],
                'title': row['title'],
                'num_of_pages': row['num_of_pages'],
                'created_at': row['books.created_at'],
                'updated_at': row['books.updated_at'],
            }
            author.books.append(book.Book(book_data))
            return author