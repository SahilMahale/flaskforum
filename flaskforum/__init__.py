from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = 'acbec8996b57af7487e6fa325b7e23de'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
log_mgr=LoginManager(app)
log_mgr.login_view='login'
log_mgr.login_message_category='info'

from flaskforum import routes
