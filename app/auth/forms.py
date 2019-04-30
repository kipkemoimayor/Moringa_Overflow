from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import Users

class RegistrationForm(FlaskForm):
    email = StringField('Email Address',validators=[Required(),Email()])
    username = StringField('Username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Register')

    def validate_email(self,data_field):
            if Users.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if Users.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username already taken')

class LoginForm(FlaskForm):
    email = StringField('Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ResetPassword(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()])
    submit = SubmitField('Reset Password')

class NewPassword(FlaskForm):
    password = PasswordField('Password',validators=[Required()])
    password_repeat = PasswordField('Repeat Password', validators=[Required(),EqualTo('password')])
    submit = SubmitField('Change Password')
