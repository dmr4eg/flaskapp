from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'SECRET KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nsiapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes  # Import routes after db initialization
from app.api_routes import api

app.register_blueprint(api)