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
    submit = SubmitField('Submit Answer')
