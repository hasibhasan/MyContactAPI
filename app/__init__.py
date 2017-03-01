from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api



app = Flask(__name__)

app.config.from_object('config')
app.secret_key = "test"

db = SQLAlchemy(app)
api = Api(app)

from app import models
from app.routes import UsersList
api.add_resource(UsersList, '/user')