# Import the class `Flask` from the `flask` module,
#  written by someone else.
from flask import Flask
from flask import render_template, request

import hashlib
import qrcode
import os


# Instantiate a new web application called `app`,
#  with `__name__` representing the current file
app = Flask(__name__)

# A decorator; when the user goes to the route `/`,
#  exceute the function immediately below


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello", methods=["POST"])
def hello():
    data = request.form.get("data")

    img = qrcode.make(data)

    data_as_bytes = str.encode(data)

    qr_hash = hashlib.md5(data_as_bytes)

    qr_filename = qr_hash.hexdigest()

    qr_path = os.path.join('static', f"{qr_filename}.png")

    img.save(qr_path)

    return render_template("hello.html", name="OK")


# @app.route("/<string:name>")
# def index(name):
#     name = name.capitalize()
#     return render_template("index.html", name=name)
