from flask import jsonify, request
from app.models import User
from flask_restful import Resource

class UsersList(Resource):
       def get(self):
        results = User.query.all()

        json_results = []
        for result in results:
            d = {'title': result.title,
                 'description': result.body
                }
            json_results.append(d)

        return jsonify(items=json_results)

       def post(self):
           user_data_json= request.get_json(force= True)
           title= user_data_json['title']
           description = user_data_json['description']
           try:
             user = User("Title 3", "Description")
             user.add(user)
             return {"result": "Successful"}
           except:
               return {"result":"Error"}










