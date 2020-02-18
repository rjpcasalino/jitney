import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, after_this_request, make_response
)
import bcrypt
import flask_login

from jitney.db import get_db, query_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

class User(flask_login.UserMixin):
    pass

def handle_signup():
    if request.form['email']:
        hashed = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        res = query_db('INSERT INTO users (email, password) VALUES(?, ?)', 
            [request.form['email'], hashed], 
            insert=True)
    return 'Check logs'

def handle_login():
    error = None;
    user = query_db('SELECT * FROM users WHERE email = ?', 
        [request.form['email']], one=True)
    if user is None:
        flash('Incorrect email or password!', error);
        return redirect(url_for('index'))
    elif bcrypt.checkpw(request.form['password'].encode('utf-8'), user[2]):
        flash('You were successfully logged in!')
        user = User()
        user.id = request.form['email']
        flask_login.login_user(user)
        return redirect(url_for('index.index'))
    else:
        flash('Incorrect email or password!', error)
        return redirect(url_for('index'))

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return handle_signup()
    return render_template('signup.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return handle_login()
    return render_template('login.html')

@bp.route('/logout')
def logout():
    flask_login.logout_user()
    return 'logged out!'
