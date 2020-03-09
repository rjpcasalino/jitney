import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        def make_dicts(cursor, row):
            return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))
        g.db.row_factory = make_dicts
    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))

def query_db(query, args=(), one=False, insert=False):
    cur = get_db().execute(query, args)
    if insert:
        cur.connection.commit()
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized database!")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
