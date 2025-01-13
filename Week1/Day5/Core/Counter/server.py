from flask import Flask, render_template, session, redirect
app =Flask(__name__)

app.secret_key = 'keep it secret'

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html', counter=session['counter'])

# Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
@app.route('/destory_session', methods=['POST'])
def destory_session():
    session.clear() # clears all keys
    return redirect('/') # redirect to the root route


if __name__=="__main__":
    app.run(debug=True)