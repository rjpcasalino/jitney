import functools
import urllib3
import json
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

@bp.route("/forecast")
def forecast():
    if request.args.get('lat') is None or request.args.get('lng') is None:
        return 'Bad Request', 400
    url = f"https://api.weather.gov/points/{request.args.get('lat')},{request.args.get('lng')}"
    r = http.request("GET", url, headers={ "User-Agent": "(jitney.cab, contact@jitney.cab)"})
    if r.data is not None:
        url = json.loads(r.data)
        print(url["properties"]["forecastHourly"])
        r = http.request("GET", url["properties"]["forecastHourly"], headers={ "User-Agent": "(jitney.cab, contact@jitney.cab)"})
        if r.data is not None:
            data = json.loads(r.data)
            return jsonify(
                    shortForecast=data["properties"]["periods"][0]["shortForecast"],
                    windSpeed=data["properties"]["periods"][0]["windSpeed"],
                    temperature=data["properties"]["periods"][0]["temperature"],
                    )
    return jsonify(error="Error: weather.gov request failed!")
