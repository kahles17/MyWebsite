from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class API(Resource):
    def get(self,A):
        return {"data":A}

api.add_resource(API,"/api/<int:A>")
if __name__ == "__main__":
    app.run()