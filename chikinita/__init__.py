from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)    # so flask knows where to find our files, instantiate flask
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from chikinita import routes