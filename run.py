'''
source /home/willian/projects/git-projects/flask-study/venv/bin/activate
'''

from flask import Flask, redirect, url_for
from app.home import home

def create_app():
    app = Flask(__name__)

    app.register_blueprint(home)

    '''
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/redirect')
    def redirect_url():
        #return redirect('http://localhost:5000/')
        return redirect(url_for('hello_world'))
    '''
    return app