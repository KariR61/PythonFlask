from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField,IntegerField
from wtforms.validators import Required,Email,NumberRange

class LoginForm(Form):
    email = StringField('Enter your email',validators=[Required(),Email()])
    passw = PasswordField('Enter password',validators=[Required()])
    submit = SubmitField('Login')
    
class RegisterForm(Form):
    email = StringField('Enter your email',validators=[Required(),Email()])
    passw = PasswordField('Enter password',validators=[Required()])
    submit = SubmitField('Register')
    
class FriendForm(Form):
    name = StringField('Enter your email',validators=[Required()])
    address = StringField('Enter your address',validators=[Required()])
    age = IntegerField('Enter friend age',validators=[Required(),NumberRange(min=0,max=155,message="Enter value between 0-115")])
    submit = SubmitField('Save')
