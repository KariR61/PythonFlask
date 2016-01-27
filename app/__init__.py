from flask import Flask

app = Flask(__name__)
#This lines configures our app using the config.py file
app.config.from_object('config')
from app import routers