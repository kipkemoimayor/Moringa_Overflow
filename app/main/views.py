from . import main
from flask import render_template,redirect,url_for
from flask_login import login_required
from .. import db
from ..models import Users


@main.route("/")
def index():
    title="Welcome to Moringa flow"

    return render_template("index.html",title=title)
