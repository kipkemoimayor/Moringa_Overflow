from . import main
from flask import render_template,redirect,url_for
from flask_login import login_required
from .. import db
from ..models import Users,Question


@main.route("/")
def index():
    title="Welcome to Moringa flow"

    return render_template("index.html",title=title)


@main.route("/questions/ask_a_question/")
def ask_a_question():
    title=f"ask a question {current_user.user}"
    #saving to the database

    question_form='form'
    if question_form.validate_on_submit():
        question=Questions(question=form.data.question,category=form.data.category)
        db.session.add(question)
        db.session.commit()

        return redirect("main.index")

    return render_template("question.html",title=title)
