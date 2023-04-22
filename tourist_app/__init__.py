from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the myapp
app = Flask(__name__)
# configure the SQLite database, relative to the myapp instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tourist_app.db"
# initialize the myapp with the extension
db.init_app(app)

from tourist_app import routes
