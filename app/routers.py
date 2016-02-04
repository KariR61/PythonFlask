from app import app
#render_template gives you access to Jinja2 template engine
from flask import render_template,request, make_response,flash,redirect,session
from app.forms import LoginForm,RegisterForm,FriendForm
from app.db_models import Users,Friends
from app import db
from flask.ext.bcrypt import check_password_hash

@app.route('/',methods=['GET','POST'])
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


@app.route('/user/<name>')
def user(name):
    print(request.headers.get('User-Agent'))
    return render_template('template_user.html',name=name)

#Example how to can define route methods
@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')
    return render_template('template_user.html',name=name)


@app.route('/register',methods=['GET','POST'])
def register():
    register = RegisterForm()
    #Check if get method
    if request.method == 'GET':
        return render_template('template_register.html',form=register,isLogged=False)
    else:
        #check if form data is valid
        if register.validate_on_submit():
            user = Users(register.email.data,register.passw.data)
            try:
                db.session.add(user)
                db.session.commit()
            except:
                db.session.rollback()
                flash('Username allready in use')
                return render_template('template_register.html',form=register,isLogged=False)
            flash("Name {0} registered.".format(register.email.data))
            return redirect('/')
        #form data was not valid
        else:
            flash('Give proper imformation to email and password fields!')
            return render_template('template_register.html',form=register,isLogged=False)



@app.route('/logout')
def logout():
    #delete user session (clear all values)
    session.clear()
    return redirect('/')
            
            

        
        
        
        
#this is comment also, but you cn use only one line
"""This is comment
    you can use multiple lines"""