import os

DEBUG = False
SECRETE_KEY='topsecrete'
SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS=False