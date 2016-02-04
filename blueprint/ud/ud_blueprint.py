from flask import Blueprint,session,redirect,request,render_template
from app.forms import FriendForm
from app import db
from app.db_models import Users,Friends

#Create blueprint
#First argument is thae name of the blueprint folder
#Second is always __name__ attribute
#Thrid parameter telss what folder contains your template
ud = Blueprint('ud',__name__,template_folder='templates',url_prefix=('/app/'))

#/app/delete
@ud.route('delete/<int:id>')
def delete(id):
    return "Delete"

@ud.route('update')
def update():
    return "Update"

def before_request():
    if not 'isLogged' in session:
        return redirect('/')


@ud.route('friends',methods=['GET','POST'])
def friends():
    form = FriendForm()
    if request.method == 'GET':
        return render_template('template_friends.html',form=form,isLogged=True)
    else:
        if form.validate_on_submit():
            temp = Friends(form.name.data,form.address.data,form.age.data,session['user_id'])
            db.session.add(temp)
            db.session.commit()
            #Tapa 2
            user = Users.query.get(session['user_id'])
            print(user.friends)
            return render_template('template_user.html',isLogged=True,friends=user.friends)
        else:
            flash('Give proper values to all fields')
            return render_template('template_friends.html',form=form,isLogged=True)


    
ud.before_request(before_request)
   