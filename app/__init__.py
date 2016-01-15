import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path(basedir, 'tmp'))
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models