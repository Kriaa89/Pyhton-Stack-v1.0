from flask import Flask, render_template, request, redirect, flash, session
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/create', methods=['POST'])
def create_user():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment'],
    }
    Dojo.save(data)
    return redirect('/')



@app.route('/results')
def results():
    all_dojos = Dojo.get_all()
    return render_template('detail.html',dojos=all_dojos)