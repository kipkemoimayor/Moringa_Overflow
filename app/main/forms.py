from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, DateField, SelectField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')


class PostQuestion(FlaskForm):
    question=TextAreaField("Your Question")
    category=SelectField("Choose category",choices=[("py","Python"),("js","JavaScript")])
    submit=SubmitField("Ask")

class AnswersForm(FlaskForm):
    solution = TextAreaField('Answer the Question')
    solution_submit = SubmitField('Submit Answer')

class QuestionForm(FlaskForm):
    title = StringField('Question title',validators=[Required()])
    category=SelectField("Choose category",choices=[("py","Python"),("js","JavaScript"),('flask','Flask'),("jquery","jQuery"),("java","Java"),('angular','Angular'),('django','Django'),('html','Html5'),('post','Postgresql')])
    question = TextAreaField('Post your question')
    submit = SubmitField('Submit')

