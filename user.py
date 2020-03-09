from flask import request
import flask_login


class User(flask_login.UserMixin):
    def ua(self):
        return request.headers["user-agent"]
    pass


user = User()
