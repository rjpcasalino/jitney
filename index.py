import functools
import time

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, after_this_request, make_response
)

import flask_login

bp = Blueprint('index', __name__, url_prefix='/')

@bp.before_request
def detect_user_language():
    language = request.cookies.get('lang')
    
    if language is None:
        language = 'en-US' ## gonna guess

        @after_this_request
        def remember_lang(response):
            response.set_cookie('lang', language)
            return response

@bp.route('/', methods=['GET', 'POST'])
def frontpage():
    if 'email' in session:
        return render_template('front.html', email=session['email'], time=time.ctime())
    return render_template('front.html', time=time.ctime())

@bp.route('/account')
@flask_login.login_required
def account():
    return render_template('account.html')
