import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, after_this_request, make_response
)

import flask_login
from . import db

bp = Blueprint("index", __name__, url_prefix="/")

@bp.before_request
def load_stories():
    g.stories = db.query_db("SELECT * FROM stories;", one=True)

@bp.route("/", methods=["GET", "POST"])
def frontpage():
    return render_template("front.html")

@bp.route("/<year>/<month>/<day>/<section>/<story>.html")
def story(year, month, day, section, story):
    return f"{year, month, day, section, story}"

@bp.route("/submit", methods=["POST"])
def submit():
    return render_template("signup.html")

@bp.route("/account")
@flask_login.login_required
def account():
    return render_template("account.html")

