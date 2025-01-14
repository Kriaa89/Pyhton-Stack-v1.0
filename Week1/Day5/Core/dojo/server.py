from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keeep it secret'


# this route will render the form
@app.route('/')
def inndex():
    return render_template('index.html')

# this route will handle the form submission
@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name'] # storing the name in session 
    session['location'] = request.form['location'] 
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

# this route will render the result template and display the form data 
@app.route('/result')
def result():
    return render_template('result.html')

if __name__ =='__main__':
    app.run(debug=True)