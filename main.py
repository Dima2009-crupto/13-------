from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

import db_actions
from db import create_db


app = Flask(__name__)
api = Api(app)


def row_to_json(clients: list):
    data = []
    for client in clients:
        data.append({
            "id": client.id,
            "name": client.name,
            "text": client.text
        })
        
    data_response = jsonify(data)
    data_response.status_code = 200
    return data_response


class clientAPI(Resource):
    def get(self, id=0):
        if  not id:
            client = db_actions.get_client(id)
            if client:
                return row_to_json([client])
        
            answer = jsonify()
            answer.status_code = 404
            return answer
    
        clients = db_actions.get_client()
        return row_to_json(clients)
        
       
    def client(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("text")    
        params = parser.parse_args()
        id = db_actions.add_client(**params)
        answer = jsonify("Статтю успішно додано під id {id}")
        answer.status_code = 200
        return answer
    
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("text")
        params = parser.parse_args()
        answer = db_actions.update_client(id, **params)
        answer = jsonify(answer)
        answer.status_code = 200
        return answer
        
   
    def delete(self, id):
        answer = jsonify(db_actions.delete_client(id))
        answer.status_code = 200        
        return answer
    
    
api.add_resource(clientAPI, "/api/gyms/","/api/gyms/<int:id>/")
    
    
if __name__ == "__main__":
    create_db()
    app.run(debug=True, port=3000)
    