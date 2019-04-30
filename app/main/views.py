from . import main
from flask import render_template
from .. import db
from flask_login import login_required,current_user

@main.route("/")
def index():
    title="Welcome to Moringa flow"

    return render_template("index.html",title=title)
