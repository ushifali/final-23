from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# create the extension
db = SQLAlchemy()
# create the myapp
app = Flask(__name__)
bcrypt = Bcrypt(app)
# configure the SQLite database, relative to the myapp instance folder
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tourist_app.db"
# initialize the myapp with the extension
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
db.init_app(app)

from tourist_app import routes
