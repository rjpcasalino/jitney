from flask import Flask, request, after_this_request, make_response, render_template
app = Flask(__name__)

def handle_account_signup(e):
    res = 'hello %s' %(e)
    return res

def handle_ask_jitney(n, f, q):
     """
     (name, from, question)
     jitney needs to take the user question
     and check 1) that user is allowed post 
     because they are registered. 2) update
     the grid with the question. 3) add 
     question to sql lite db for easy access?
     """

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
        if request.form['email'] == 'ryan@boringtranquility.io':
            return handle_account_signup(request.form['email'])
        return 'Hi, Stranger!'
    else:
        return render_template('index.html', browser=browser)
