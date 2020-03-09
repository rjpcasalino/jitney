import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, after_this_request, make_response
)
import bcrypt
import flask_login

from jitney.db import get_db, query_db
from .user import User

bp = Blueprint("books", __name__, url_prefix="/books")


@bp.route("/", methods=["GET", "POST"])
def books():
    return render_template("books.html")
