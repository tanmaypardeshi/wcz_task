from apis import api
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello"}


api.add_resource(HelloWorld, "/")
