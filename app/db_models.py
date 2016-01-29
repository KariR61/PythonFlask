
from app import db

class Users(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(128),unique=True)
    passw = db.Column(db.String(128))
    
    def __init__(self,email, passw):
        self.email = email
        self.passw = passw
        
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