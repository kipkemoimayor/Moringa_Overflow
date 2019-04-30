from . import main
from flask import render_template
from .forms import CommentsForm


@main.route("/")
def index():
    title="Welcome to Moringa flow"

    return render_template("index.html",title=title)

@main.route("/new/comment",methods=["GET","POST"])
def comment():
    
    comment_form = CommentsForm()

    return render_template("new_comment.html", comment_form = comment_form)