#coding:utf-8

from flask_restful import Api

from handlers.example import ExampleEndpoint

api = Api()

api.add_resource(ExampleEndpoint,   "/api/example")
