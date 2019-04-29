from . import main
from flask import render_template,redirect,url_for
from flask_login import login_required
from .. import db
from ..models import Users


@main.route("/")
def index():
    title="Welcome to Moringa flow"

    return render_template("index.html",title=title)


#registration
@main.route("/register")
def register():
    form="form name"
    if form.validate_on_submit():
        roles="Users";
        user=Users(email=form.email.data,username=form.username.data,password=form.password.data,role_id=roles)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("auth/register",form=form)



'''
login users
'''
