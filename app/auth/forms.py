class ReviewForm(FlaskForm):

 title = StringField('Review title',validators=[Required()])

 review = TextAreaField('Overflow review')

 submit = SubmitField('Submit')
