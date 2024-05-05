from flask import Flask
from flask_bootstrap import Bootstrap
from .api_routes import api

app = Flask(__name__)
Bootstrap(app)
app.register_blueprint(api)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nsiapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import routes

from flask_sqlalchemy import SQLAlchemy