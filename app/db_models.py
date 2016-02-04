
from app import db
from flask.ext.bcrypt import generate_password_hash

class Users(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(128),unique=True)
    passw = db.Column(db.String(128))
    
    friends = db.relationship('Friends',backref='user',lazy='dynamic')
    
    def __init__(self,email, passw):
        self.email = email
        self.passw = generate_password_hash(passw)
    #def __str__(self):
        #return self.email + '' + self.passw + '' + str(self.id)
        
class Friends(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    age = db.Column(db.Integer)
    user_id= db.Column(db.Integer,db.ForeignKey('users.id'))
    #This is Friends constructor
    def __init__(self,name,address,age,user_id):
        self.name = name
        self.address = address
        self.age = age
        self.user_id = user_id