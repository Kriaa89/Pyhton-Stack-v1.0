from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', rows=8, columns=8, colorx='red', colory='black')

@app.route('/<int:x>')
def display_4(x):
    return render_template('index.html', rows=x, columns=8, colorx='red', colory='black')

@app.route('/<int:x>/<int:y>')
def display_x_y(x, y):
    return render_template('index.html', rows=x, columns=y, colorx='red', colory='black')

if __name__=="__main__":  
    app.run(debug=True, port=5001)   