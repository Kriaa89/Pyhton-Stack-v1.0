from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    if not Email.validate_email(request.form):
        return redirect('/')
    data = {
        "email": request.form['email']
    }
    Email.save(data)
    return redirect('/success')


@app.route('/success')
def success():
    all_emails = Email.get_all()
    return render_template('success.html', email= all_emails)