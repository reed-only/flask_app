"""
Create Flask app and database
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://flask_user:flask_password@mysql:3306/flask_app'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
