from . import db


'''
table for users
'''
class Users(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    pass_secure=db.Column(db.String(255))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))


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
