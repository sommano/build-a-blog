from flask import Flask, request, redirect,render_template
from flask_sqlalchemy import SQLAlchemy
import cgi
import os

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods = ["POST", "GET"])
def index():
    return render_template("blog.html")

@app.route("/newpost", methods = ["POST", "GET"])
def new():
    return render_template("newpost.html")

@app.route("/blog", methods = ["POST", "GET"])
def blog():
    return render_template("blog.html")



if __name__ == '__main__':
    app.run()