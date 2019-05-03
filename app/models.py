from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
import os
from time import time
from datetime import datetime

'''
geting the users by id
'''
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

'''
table for users
'''
class Users(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),index=True)
    email=db.Column(db.String(255),unique=True,index=True)
    profile_pic_path = db.Column(db.String())
    pass_secure=db.Column(db.String(255))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    questions=db.relationship('Question',backref='user',lazy='dynamic')
    answers=db.relationship('Answers',backref='owner',lazy='dynamic')
    # moringa_overflow = db.relationship('moringa_overflow', backref='author', lazy='dynamic')
    # comments = db.relationship('Comments', backref='author', lazy='dynamic')




    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self,password):
        self.pass_secure =generate_password_hash(password)

    def set_password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def get_reset_password_token(self, expires_in=6000):
        return jwt.encode({'reset_password':self.id, 'exp':time()+expires_in}, os.environ.get('SECRET_KEY'), algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password(token):
        try:
            id = jwt.decode(token,"collo",algorithms=['HS256'])['reset_password']
        except:
            return
        return Users.query.get(id)


    def __repr__(self):
        return f'Users {self.username}'


'''
Roles within users
'''

class Role(db.Model):
    __tablename__="roles"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(220))
    users=db.relationship('Users',backref='role',lazy='dynamic')

    def add():
        admin=Role(name="Admin")
        user=Role(name="Users")
        db.session.add_all([admin,user])
        db.session.commit()


    def __repr__(self):
        return f'Users {self.name}'


'''
model for Questions
'''

class Question(db.Model):
    __tablename__='questions'
    id=id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String())
    question=db.Column(db.String())
    category=db.Column(db.String())
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    answers=db.relationship('Answers',backref='quiz',lazy='dynamic')
    posted = db.Column(db.DateTime,default=datetime.utcnow)



'''
model for solutions
'''

class Answers(db.Model):
    __tablename__='answers'
    id=db.Column(db.Integer,primary_key=True)
    solution=db.Column(db.String())
    question_id=db.Column(db.Integer,db.ForeignKey('questions.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    comments=db.relationship('Comments',backref='commen',lazy='dynamic')
    comments=db.relationship('Votes',backref='vote',lazy='dynamic')
    posted = db.Column(db.DateTime,default=datetime.utcnow)


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime(250), default=datetime.utcnow)
    moringa_overflow_id = db.Column(db.Integer, db.ForeignKey("moringa_overflow.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        comments = Comments.query.filter_by(moringa_overflow_id=id).all()
        return comments

class Votes(db.Model):
    __tablename__='votes'
    comment=db.Column(db.String())
    id=db.Column(db.Integer,primary_key=True)
    votes_userid=db.Column(db.Integer)
    ans_id=db.Column(db.Integer,db.ForeignKey('answers.id'))


'''
models for comments
'''

class Comments(db.Model):
    __tablename__='comments'
    id=id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String())
    answer_id=db.Column(db.Integer,db.ForeignKey('answers.id'))
