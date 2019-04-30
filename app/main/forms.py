from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, DateField, SelectField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')

class QuestionForm(FlaskForm):
    question_title = StringField('Question title',validators=[Required()])
    question = TextAreaField('Post your question')
    submit = SubmitField('Submit')
