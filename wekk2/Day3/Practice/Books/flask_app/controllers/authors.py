from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    all_authors = Author.get_all()
    return render_template("authors.html", authors=all_authors)

@app.route('/author/create', methods=['POST'])
def create_author():
    data = {
        "name": request.form['name']
    }
    Author.save(data)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def show_author(id):
    data = {
        "id": id
    }
    author = Author.get_by_id(data)
    favorite_books = author.get_favorites_books(data)
    # Only get books that aren't favorites yet for the dropdown
    all_books = Book.get_unfavorited_books(data)
    return render_template("add_author.html", author=author, favorite_books=favorite_books, all_books=all_books)

@app.route('/authors/<int:id>/add_favorite', methods=['POST'])
def add_favorite(id):
    data = {
        'author_id': id,
        'book_id': request.form['book_id']
    }
    Author.add_favorite_book(data)
    return redirect(f'/authors/{id}')