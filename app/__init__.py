from flask import Flask
from flask_bootstrap import Bootstrap
from .api_routes import api

app = Flask(__name__)
Bootstrap(app)
app.register_blueprint(api)

from app import routes
