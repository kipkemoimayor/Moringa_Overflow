from . import main
from flask import render_template


@main.route("/")
def index():
    title="Welcome to Moringa flow"

    return render_template("index.html",title=title)
