import os
import time
import sqlite3
import bcrypt
from flask import Flask, request, after_this_request, make_response, render_template, flash, redirect, url_for, g, session

app = Flask(__name__)

app.secret_key = os.environ['APP_KEY']
DATABASE = os.environ['JITNEY_DB']

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

def query_db(query, args=(), one=False, insert=False):
    cur = get_db().execute(query, args)
    if insert:
        cur.connection.commit()
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def handle_signup():
    ## insert user into users
    ## with hashed password
    ## 
    res = query_db('INSERT INTO users (email, password) VALUES(?, ?)', ['ryan', 'test'], insert=True)
    return 'Check logs'

def handle_login():
    error = None;
    user = query_db('SELECT * FROM users WHERE email = ?', 
        [request.form['email']], one=True)
    if user is None:
        flash('Incorrect email or password!', error);
    elif request.form['password'] == user[2]:
        flash('You were successfully logged in!')
        session['email'] = request.form['email']
        return redirect(url_for('index'))
    else:
        flash('Incorrect email or password!', error)
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
    if request.method == 'POST':
        return handle_signup()
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
