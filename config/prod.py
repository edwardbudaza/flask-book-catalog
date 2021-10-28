import os
import re

DEBUG = False
SECRETE_KEY='topsecrete'
SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
SQLALCHEMY_TRACK_MODIFICATIONS=False