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


@main.route("/questions/ask_a_question/",methods=['POST','GET'])
@login_required
def ask_a_question():
    title=f"ask a question {current_user.username}"
    # saving to the database

    question_form = QuestionForm()
    if question_form.validate_on_submit():
        question=Question(question=question_form.question.data,category=question_form.category.data,title=question_form.title.data,user_id=current_user.id)
        db.session.add(question)
        db.session.commit()

        return redirect(url_for('main.feeds'))

    return render_template("new_question.html", question_form = question_form)

@main.route("/new/comment",methods=["GET","POST"])
def comment():

    comment_form = CommentsForm()
    if comment_form.validate_on_submit():
        comment=Comments(comment=comment_form.comment.data)
        db.session.add(comment)
        db.session.commit()


    return render_template("new_comment.html", comment_form = comment_form)



@main.route("/question/answer_a_question/<int:id>/",methods=["GET","POST"])
def answer_a_question(id):
    question=Question.query.filter_by(id=id).first()
    answer=Answers.query.filter_by(question_id=id).all()
    answer_form = AnswersForm()
    if answer_form.validate_on_submit():
        answer = Answers(solution=answer_form.solution.data,question_id = question.id, user_id = current_user.id)
        db.session.add(answer)
        db.session.commit()
        return redirect (url_for('main.answer_a_question',id=question.id))

    return render_template("answers.html",comment_form=answer_form,question=question,answer=answer)


@main.route("/feeds/questions",methods=['GET','POST'])
def feeds():

    all_feeds=Question.query.all()
    all_feeds.reverse()

    count_feed=Answers.query.filter_by(question_id=1).all()
    arr=[]
    for i in count_feed:
        arr.append(1)

    question_count=sum(arr)





    title="Feeds"
    return render_template("question.html",title=title,all_feeds=all_feeds,question_count=question_count)


@main.route('/user/<uname>')
def profile(uname):

    '''
    query questions for each user
    '''
    personal_quiz=Question.query.filter_by(user_id=current_user.id).all()
    user = Users.query.filter_by(username = uname).first()

    title = f"{uname.capitalize()}'s Profile"



    if user is None:
        abort(404)

    return render_template('/profile/profile.html', user = user,personal_quiz=personal_quiz, title=title)


'''
category view
'''

@main.route("/feeds/category/<categ>")
def categories(categ):
    categ=categ
    #categories
    flask=Question.query.filter_by(category='flask').all()
    python=Question.query.filter_by(category='py').all()
    javascript=Question.query.filter_by(category='js').all()
    jQuery=Question.query.filter_by(category='jquery').all()
    java=Question.query.filter_by(category='java').all()
    angular=Question.query.filter_by(category='angular').all()
    django=Question.query.filter_by(category='django').all()
    html5=Question.query.filter_by(category='html').all()
    postgresql=Question.query.filter_by(category='post').all()


    title="categories"
    return render_template("categories.html",flask=flask,python=python,categ=categ,javascript=javascript,jQuery=jQuery,java=java,angular=angular,django=django,html5=html5,postgresql=postgresql)
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


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
