from flask import Flask, request, after_this_request, make_response, render_template, flash, redirect, url_for
import time
app = Flask(__name__)
## TODO: env var
app.secret_key = b'somethingBASAazz/1a!!'

def handle_account_signup(e):
    res = 'hello %s' %(e)
    return res

def handle_login():
    error = None;
    if request.method == 'POST':
        if request.form['email'] == 'admin@mail.com':
            flash('You were successfully logged in!')
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
    for i in dir(request):
        if i == 'headers':
            print(request.headers)
    browser = request.user_agent.browser

    if request.method == 'POST':
        return handle_login()
    else:
        return render_template('index.html', browser=browser, time=time.ctime())
