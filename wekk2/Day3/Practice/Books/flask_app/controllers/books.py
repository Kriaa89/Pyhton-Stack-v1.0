from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author


@app.route('/books')
def books():
    all_books = Book.get_all()
    return render_template("books.html", books = all_books)


@app.route('/books/create', methods = ['POST'])
def create_book():
    data = {
        "title": request.form['title'],
        "num_of_pages": request.form['num_of_pages']
    }
    book = Book.get_by_id(data)
    favorite_authors = book.get_favorites_authors(data)
    all_authors = Author.get_all()
    return render_template("add_book.html", book =book,  favorite_authors=favorite_authors, all_authors=all_authors)


@app.route('/books/<int:id>/add_author', methods = ['POST'])
def add_favorite_author(id):
    data = {
        "book_id": id,
        "auhtor_id": request.form['author_id']
    }
    Book.add_favorite_athor(data)
    return redirect(f'/books/{id}')