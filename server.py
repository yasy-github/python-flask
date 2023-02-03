from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

def do_the_login():
    return 'Do the login'

def show_the_login_form():
    return 'Show login form'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/user/<username>')
def show_user_profile(username):
    return f'{escape(username)} \'s profile'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='Whang Yasy'))
    print(url_for('static', filename='style.css'))
    
