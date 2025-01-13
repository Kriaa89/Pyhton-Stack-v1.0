from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret'


@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    if 'attemp' not in session:
        session['attemp'] = 0
        return render_template('index.html')
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['attemp'] += 1 
    guess = int(request.form['guess'])
    if guess < session['number']:
        session['result'] = 'too low'
    elif guess > session['number']:
        session['result'] = 'too high'
    else:
        session['result'] = str(guess) + ' was the number!'
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)