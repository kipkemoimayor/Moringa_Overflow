from . import main
from flask import render_template,redirect,url_for
from flask_login import login_required,current_user
from .. import db
from ..models import Users,Question,Answers,Comments
from .forms import CommentsForm,AnswersForm



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

@main.route("/new/comment",methods=["GET","POST"])
def comment():

    comment_form = CommentsForm()

    return render_template("new_comment.html", comment_form = comment_form)

@main.route("question/answer_a_question/",methods=["GET","POST"])
def answer_a_question():

    answer_form = AnswersForm()
    if answer_form.validate_on_submit():
        answer = Answers(answer=form.solution.data,question_id = questions.id, user_id = users.id)
        return redirect (url_for('main.answer_a_question'))

    return render_template("answers.html")


