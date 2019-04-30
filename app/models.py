from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
import os
from time import time

'''
geting the users by id
'''
@login_manager.user_loader
def load_user(user_id):
    return Users.query(int(user_id))

'''
table for users
'''
class Users(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),index=True)
    email=db.Column(db.String(255),unique=True,index=True)
    pass_secure=db.Column(db.String(255))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError("You cannot red the password attribute")

    @password.setter
    def password(self,password):
        self.pass_secure =generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def get_reset_password_token(self, expires_in=600):
        return jwt.encode({'reset_password':self.id, 'exp':time()+expires_in}, os.environ.get('SECRET_KEY'), algorithm='HS256').decode('utf-8')

    def set_password(self,password):
        self.hash_pass = generate_password_hash(password)
    @staticmethod
    def verify_reset_password(token):
        try:
            id = jwt.decode(token, os.environ.get('SECRET_KEY'),algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


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

    def __repr__(self):
        return f'Users {self.name}'


'''
model for Questions
'''

class Question(db.Model):
    __tablename__='questions'
    id=id=db.Column(db.Integer,primary_key=True)
    question=db.Column(db.String())
    category=db.Column(db.String())


'''
model for solutions
'''

class Answers(db.Model):
    id=id=db.Column(db.Integer,primary_key=True)
    solution=db.Column(db.String())



'''
models for comments
'''

class Comments(db.Model):
    id=id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String())


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# class User(UserMixin,db.Model):
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(100))
#     email = db.Column(db.String(255),unique = True, index = True)
#     bio = db.Column(db.String(255))
#     profile_pic_path = db.Column(db.String())
#     password_hash = db.Column(db.String(255))
#
#     @property
#     def password(self):
#         raise AttributeError('You cannot read the password attritube')
#
#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def set_password(self,password):
#         self.hash_pass = generate_password_hash(password)
#
#     def verify_password(self,password):
#         return check_password_hash(self.password_hash,password)
#
#     def get_reset_password_token(self, expires_in=600):
#         return jwt.encode({'reset_password':self.id, 'exp':time()+expires_in}, os.environ.get('SECRET_KEY'), algorithm='HS256').decode('utf-8')

    # @staticmethod
    # def verify_reset_password(token):
    #     try:
    #         id = jwt.decode(token, os.environ.get('SECRET_KEY'),algorithms=['HS256'])['reset_password']
    #     except:
    #         return
    #     return User.query.get(id)
    #
    # def __repr__(self):
    #     return f'User {self.username}'
