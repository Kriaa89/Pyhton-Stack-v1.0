from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html', boxes=3, colors="blue")

@app.route('/play/<int:x>')
def play_boxes(x):
    return render_template('index.html', boxes=x, colors="blue")

@app.route('/play/<int:x>/<color>')
def play_color(x, color):
    return render_template('index.html', boxes=x, colors=color)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
# pip list, if flask exist pip uninstall flask, y, pipenv shell