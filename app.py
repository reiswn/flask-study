from flask import Flask, redirect, url_for

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/redirect')
    def redirect_url():
        #return redirect('http://localhost:5000/')
        return redirect(url_for('hello_world'))

    return app