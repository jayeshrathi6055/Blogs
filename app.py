from crypt import methods
from flask import Flask,render_template, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
import os
from markupsafe import escape

app = Flask(__name__)

# Mongodb Connection
# mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/todo_db")
# db = mongodb_client.db

# Home Page
@app.route("/", methods=['Get'])
def portfolio():
    files = os.listdir("./templates/blogs/")
    files = [file.replace(".html","") for file in files]
    return render_template(escape('index.html'),blogs = files)

# Blog Page
@app.route("/blogs/<slug>", methods=['Get'])
def baseBlog(slug):
    files = os.listdir("./templates/blogs/")
    slug = slug.replace("-","_")
    if slug+".html" in files:
        return render_template(escape(f"./blogs/{slug}.html"))
    else:
        return render_template("./invalid_route.html")

# Not Found Handler
@app.errorhandler(404)
def invalid_route(e):
    return render_template("./invalid_route.html")

# @app.route("/person")
# def person():
#     todos = db.todos.find()
#     todos = list(todos)
#     return dumps(todos)