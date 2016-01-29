import os

basedir = os.path.abspath(os.path.dirname(__file__))

SERVER_NAME='localhost:3000'
SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'data.db')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')
