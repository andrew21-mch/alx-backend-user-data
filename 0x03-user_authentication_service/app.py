#!/usr/bin/env python3
from flask import Flask
import flask
import requests
app = Flask(__name__)

@app.route("/")
def home():
    data = {"message": "Hello World!"}
    return flask.jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")