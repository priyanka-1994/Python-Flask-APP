from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# install it --> pip install flask-bcrypt
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# how to create secret key? --> python --> import os --> os.urandom(12).hex()
app.config['SECRET_KEY'] = '239e801593ec0653a918bc0f'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from market import routes
from market import models