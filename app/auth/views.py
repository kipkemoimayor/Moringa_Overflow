from flask import render_template,redirect,url_for, flash,request
from .forms import LoginForm,RegistrationForm
from . import auth
from flask_login import login_user,logout_user,login_required

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
   

    return render_template('auth/login.html',login_form = login_form)


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
  

        return redirect(url_for('auth.login'))

    title = "New Account"

    return render_template('auth/register.html',registration_form = form, title = title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))