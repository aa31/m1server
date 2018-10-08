# encoding: utf-8
import os

DEBUG = True
SECRET_KEY = os.urandom(24)

DB_URL = 'mysql://root:mm123465@localhost/m1'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mm123465@localhost/m1'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_AS_ASCII = False




