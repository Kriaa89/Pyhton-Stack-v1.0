from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def say(name):
    return "Hi  " + name + "!"
@app.route('/repeat/<name>/<int:num>')
def repeat(name, num):
    return f"hello, {name * num}"


if __name__=="__main__":  
    app.run(debug=True, port=5001)    