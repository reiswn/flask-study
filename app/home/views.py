from . import home

@home.route('/home')
def home_page():
    return 'index page'