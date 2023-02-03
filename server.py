from flask import Flask, url_for, request, render_template, redirect, session
from markupsafe import escape
import os

app = Flask(__name__)

app.config.from_pyfile('settings.py')
print('===>', app.config.get('SECRET_KEY'))     # to access environment variables


@app.route('/')
def index():
    if 'username' in session:
        # flash('You were successfully logged in')  # Message Flashing
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    error = None
    # if request.method == 'POST':
        # print(request.form['username'])
    print('===>', request.method)
    print('===>', request.args.get('key', ''))

    return render_template('hello.html', name=name, error=error)

def show_the_login_form():
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        return show_the_login_form()

@app.route('/logout')
def logout():
    app.logger.debug('A value for debugging')   # use pre-configured 'Logging' module
    session.pop('username', None)

    return redirect(url_for('index'))

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

# URL Building
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login', next='/'))
#     print(url_for('show_user_profile', username='Whang Yasy'))
#     print(url_for('static', filename='style.css'))

