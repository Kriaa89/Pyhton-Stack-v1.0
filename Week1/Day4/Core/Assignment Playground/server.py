from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index():
    return render_template('index.html', num_boxes=3, color='blue')

@app.route('/play/<int:num>')
def play_x(num):
    return render_template('index.html', num_boxes=num, color='red')

@app.route('/play/<int:num>/<color>')
def play_num_color(num, color):
    return render_template('index.html', num_boxes=num, color=color)











if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 