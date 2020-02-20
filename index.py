import functools
import time
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, after_this_request, make_response
)

import flask_login
from . import db

bp = Blueprint('index', __name__, url_prefix='/')
@bp.before_request
def load_stories():
    g.stories = db.query_db('SELECT * FROM stories;', one=True)

@bp.route('/', methods=['GET', 'POST'])
def frontpage():
    return render_template('front.html', time=time.ctime())

@bp.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    return request.form  

@bp.route('/account')
@flask_login.login_required
def account():
    return render_template('account.html')
