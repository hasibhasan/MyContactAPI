from flask import jsonify
from app.models import User
from flask_restful import Resource

class UsersList(Resource):
       def get(self):
        users_query = User.query.all()
        print users_query
        return jsonify()




