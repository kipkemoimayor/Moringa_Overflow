from .import auth
from flask import render_template,redirect,url_for,flash,request
from flask_login import login_required,login_user,login_user
from .. import db
from ..models import Users


'''
login users
'''
@auth.route("/login")
def login():
    loginForm=LoginForm()
    if loginForm.validate_on_submit():
        user = Users.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Moringa flow login"
    return render_template('auth/login.html',login_form = login_form,title=title)

#registration
@auth.route("/register")
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        roles="Users";
        user=Users(email=form.email.data,username=form.username.data,password=form.password.data,role_id=roles)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("auth/register",form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
