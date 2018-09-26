# encoding: utf-8
import os

DEBUG = True
SECRET_KEY = os.urandom(24)

# 'mysql+mysqlconnector://username:pwd@addr:port/dbname'
DB_URL = 'mysql://root:mm123465@localhost/m1'

# SQLALCHEMY_DATABASE_URI = 'mysql:pymysql//root:mm123465@localhost/m1'
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_COMMIT_TEARDOWN = True
HOST = '0.0.0.0'
PORT = 9909



