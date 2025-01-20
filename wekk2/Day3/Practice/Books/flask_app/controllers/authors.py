from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/authors')
def authors():
    all_athors = Author.get_all()
    return render_template("authors.html", authors = all_athors)


@app.route('/author/create', methods = ['POST'])
def create_author():
    data = {
        "name": request.form
    }
    Author.save(data)
    return redirect('/authors')


@app.route('/authors/<int:id>')
def show_author(id):
    data = {
        "id":id
    }
    author = Author.get_by_id(data)
    favorits_books = Author.get_favorites_books(data)
    all_books = Book.get_all()
    return render_template("add_author.html", author = author, favorits_books = favorits_books, all_books = all_books)

@app.route('/authors/<int:id>/add_favorite')
def add_favorite(id):
    data = {
        'author_id': id,
        'book_id': request.form['author_id'] # 
    }
    Book.add_favorite_athor(data)
    return redirect('/')