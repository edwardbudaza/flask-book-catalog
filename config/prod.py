import os
import re
import psycopg2

DEBUG = False
SECRETE_KEY='topsecrete'
SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

conn = psycopg2.connect(SQLALCHEMY_DATABASE_URI, sslmode='require')
SQLALCHEMY_TRACK_MODIFICATIONS=False