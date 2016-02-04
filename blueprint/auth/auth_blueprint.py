from flask import Blueprint,render_template,flash,request,redirect
from app.forms import LoginForm,RegisterForm
from app.db_models import Users,Friends
from app import db
#Create blueprint
#First argument is thae name of the blueprint folder
#Second is always __name__ attribute
#Third parameter telss what folder contains your template
auth = Blueprint('auth',__name__,template_folder='templates')


@auth.route('/',methods=['GET','POST'])
def index():
    login = LoginForm()
    #Check if get method
    if request.method == 'GET':
        return render_template('template_index.html',form=login,isLogged=False)
    else:
        #check if form data is valid
        if login.validate_on_submit():
            #Check if corret username and password
            user = Users.query.filter_by(email=login.email.data)
            if (user.count() == 1) and (check_password_hash(user[0].passw,login.passw.data)):
                print(user[0])
                session['user_id'] = user[0].id
                session['isLogged'] = True
                #Tapa 1
                friends = Friends.query.filter_by(user_id=user[0].id)
                print(friends)
                return render_template('template_user.html',isLogged=True,friends=friends)
            else:
                flash('Wrong email or password')
                return render_template('template_index.html',form=login,isLogged=False)
        #form data was not valid
        else:
            flash('Give proper imformation to email and password fields!')
            return render_template('template_index.html',form=login,isLogged=False)

