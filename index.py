import sqlite3
from flask import Flask, request, after_this_request, make_response, render_template, flash, redirect, url_for, g, session
import time
app = Flask(__name__)
## TODO: env var
app.secret_key = b'somethingBASAazz/1a!!'
DATABASE = './database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def handle_account_signup(e):
    res = 'hello %s' %(e)
    return res

def handle_login():
    error = None;
    print(request.form)
    if request.form['email'] == 'admin@mail.com':
        flash('You were successfully logged in!')
        session['email'] = request.form['email']
        return redirect(url_for('index'))
    else:
        flash('ERROR', error)
        return redirect(url_for('index'))

@app.before_request
def detect_user_language():
    language = request.cookies.get('lang')
    
    if language is None:
        language = 'en-US' ## gonna guess

        @after_this_request
        def remember_lang(response):
            response.set_cookie('lang', language)
            return response

@app.route('/', methods=['GET', 'POST'])
def index():
    cur = get_db().cursor()
    print(dir(cur))
    print(cur.fetchall())
    for i in dir(request):
        if i == 'headers':
            print(request.headers)
    browser = request.user_agent.browser

    if request.method == 'POST':
        return handle_login()
    else:
        if 'email' in session:
            return render_template('index.html', email=session['email'], time=time.ctime())
        return render_template('index.html', time=time.ctime())

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return handle_login()
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return 'logged out!'
