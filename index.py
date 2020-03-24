import functools
import urllib3
from flask import (
    Blueprint, flash, current_app, g, redirect, render_template, request, session, url_for, after_this_request, make_response, jsonify
)

import flask_login
from . import db

bp = Blueprint("index", __name__, url_prefix="/")

http = urllib3.PoolManager()

@bp.before_request
def load_stories():
    g.lead_stories = db.query_db(
        "SELECT title, headline, byline, preview, publishYear, publishMonth, publishDay FROM stories WHERE lead = 1;")
    g.darksky_api = "10e290e9e7bcc2b71c38684cc11a171c"


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

@bp.route("/morning")
def morning():
    if request.args.get('lat') is None or request.args.get('lng') is None:
        return 'Bad Request', 400
    url = f"https://api.darksky.net/forecast/{current_app.config['DARKSKY_API']}/{request.args.get('lat')},{request.args.get('lng')}"
    r = http.request("GET", url)
    return r.data
