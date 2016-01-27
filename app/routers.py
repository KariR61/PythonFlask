from app import app
#render_template gives you access to Jinja2 template engine
from flask import render_template,request, make_response

@app.route('/')
def index():
    name = 'Markus'
    address = 'Rautatienkatu'
    response = make_response(render_template('template_index.html',name=name,title=address))
    response.headers.add('Cache_Control','no-cache')
    return response

@app.route('/user/<name>')
def user(name):
    print(request.headers.get('User-Agent'))
    return render_template('template_user.html',name=name)

#Example how to can define route methods
@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')
    return render_template('template_user.html',name=name)

#this is comment also, but you cn use only one line
"""This is comment
    you can use multiple lines"""