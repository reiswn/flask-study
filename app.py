from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/redirect')
def redirect_url():
    #return redirect('http://localhost:5000/')
    return redirect(url_for('hello_world'))

app.run(debug=True)