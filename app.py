from flask import Flask
from flask_restfule import Api, Resource

app = Flask(__name__)
api = Api(app)

class API(Resource):
    def get(self):
        return {"data":A}

api.add_resource(API,"/api/<int:A>")