from . import home
from flask.templating import render_template

@home.route('/home')
@home.route('/home/<name>')
def home_page(name=None):
    page = "Home Page"
    numbers = [1,2,4,8,16,32,64]

    return render_template('home.html', page_var=page, numbers_var=numbers, name=name)