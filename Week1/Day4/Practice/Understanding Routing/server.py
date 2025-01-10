from flask import Flask
app = Flask(__name__)
# localhost:5000/ - have it say "Hello World!"
@app.route('/')
def index():
    return 'Hello World'

# localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# localhost:5000/say/flask - have it say "Hi Flask!"

@app.route('/say/<name>')
def say(name):
    return "Hi  " + name + "!"

# Create one url pattern and function that can handle the following examples 
# (HINT: path variables are by default passed as strings. How might you handle a number?):
@app.route('/repeat/<name>/<int:num>')
def repeat(name, num):
    return f"hello, {name * num}"


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.