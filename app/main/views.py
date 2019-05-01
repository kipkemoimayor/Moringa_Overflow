from . import main
from flask import render_template,redirect,url_for,abort,flash,request
from flask_login import login_required,current_user
from .. import db,photos
from ..models import Users,Question,Comments,Answers
from .forms import CommentsForm,PostQuestion,AnswersForm,QuestionForm



@main.route("/")
def index():
    title="Welcome to Moringa flow"

    return render_template("index.html",title=title)


@main.route("/questions/ask_a_question/")
def ask_a_question():
    # title=f"ask a question {current_user.user}"
    #saving to the database

    question_form = QuestionForm()
    # if question_form.validate_on_submit():
    #     question=Question(question=question_form.data.question,category=question_form.data.category)
    #     db.session.add(question)
    #     db.session.commit()

        # return redirect("main.index", question_form = question_form)

    return render_template("new_question.html", question_form = question_form)

@main.route("/new/comment",methods=["GET","POST"])
def comment():

    comment_form = CommentsForm()
    if comment_form.validate_on_submit():
        comment=Comments(comment=comment_form.comment.data)
        db.session.add(comment)
        db.session.commit()


    return render_template("new_comment.html", comment_form = comment_form)



@main.route("/ask",methods=['POST','GET'])
def ask_quiz():
    title="Ask a Quiz"
    form=PostQuestion()
    if form.validate_on_submit():
        quiz=Question(question=form.question.data,category=form.category.data)
        db.session.add(quiz)
        db.session.commit()
        return redirect(url_for('main.ask_quiz'))
    return render_template("post.html",title=title,form=form)

@main.route("/question/answer_a_question/",methods=["GET","POST"])
def answer_a_question():

    answer_form = AnswersForm()
    if answer_form.validate_on_submit():
        answer = Answers(answer=form.solution.data,question_id = questions.id, user_id = users.id)
        return redirect (url_for('main.answer_a_question'))

    return render_template("answers.html")


@main.route("/feeds/questions",methods=['GET','POST'])
def feeds():

    title="Feeds"
    return render_template("question.html",title=title)

@main.route('/user/<uname>&<id_user>')
@login_required
def profile(uname, id_user):
    user = Users.query.filter_by(username = uname).first()

    title = f"{uname.capitalize()}'s Profile"

    

    if user is None:
        abort(404)
    
    return render_template('index.html', user = user, title=title)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = Users.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
