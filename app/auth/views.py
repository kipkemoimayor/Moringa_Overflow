from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import Users
from .forms import RegistrationForm,LoginForm,ResetPassword,NewPassword
from .. import db
from ..email import send_email, send_reset_email
from flask_login import login_user,logout_user,login_required,current_user
import os

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = Users.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get("next") or url_for("main.index"))

        flash('Invalid username or Password')

    title = "Blog-It Login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()



        return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/register.html',registration_form = form, title = title)

# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for("main.index"))

@auth.route('/reset',methods=['GET','POST'])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPassword()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            send_reset_email(user)
            flash('Check email on how to reset password')
            return redirect(url_for('auth.login'))
        elif not user:
            flash('The email does not exist')
    return render_template('auth/reset.html',title='Reset Password',form=form)

@auth.route('/new_password/<token>', methods=['GET','POST'])
def new_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = Users.verify_reset_password(token)
    if not user:
        return redirect(url_for('main.index'))
    form = NewPassword()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset')
        return redirect(url_for('auth.login'))
    return render_template('auth/change_password.html',title='Reset Password',form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
