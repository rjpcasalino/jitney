import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, after_this_request, make_response
)
import bcrypt
import flask_login

from jitney.db import get_db, query_db
from .user import User

bp = Blueprint("auth", __name__, url_prefix="/auth")

def handle_signup():
    if request.form["email"]:
        hashed = bcrypt.hashpw(request.form["password"].encode("utf-8"), bcrypt.gensalt())
        res = query_db("INSERT INTO users (email, password) VALUES(?, ?)", 
            [request.form["email"], hashed], 
            insert=True)
    return "check logs"

def handle_login():
    user = query_db("SELECT * FROM users WHERE email = ?", 
        [request.form["email"]], one=True)
    if user is None:
        flash("Whoops! Incorrect email or password.");
        return redirect(url_for("index.frontpage"))
    elif bcrypt.checkpw(request.form["password"].encode("utf-8"), user[2].encode("utf-8")):
        user = User()
        user.id = request.form["email"]
        user.ip = request.headers
        flask_login.login_user(user)
        return redirect(url_for("index.frontpage"))
    else:
        flash("Whoops! Incorrect email or password.")
        return redirect(url_for("index.frontpage"))

@bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        return handle_signup()
    return render_template("signup.html")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return handle_login()
    return render_template("login.html")

@bp.route("/logout")
def logout():
    flask_login.logout_user()
    return redirect(url_for("auth.login"))
