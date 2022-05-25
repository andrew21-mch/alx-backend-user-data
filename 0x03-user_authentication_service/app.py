#!/usr/bin/env python3
from flask import Flask
import flask
import requests
app = Flask(__name__)
from sqlalchemy import create_engine


from auth import Auth


AUTH = Auth()

@app.route("/")
def home():
    data = {"message": "Hello World!"}
    return flask.jsonify(data)

@app.route('/user')
def user():
    r = requests.post(AUTH.register_user("drew12@gmail.com", "12342"))
    return flask.jsonify(r)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")