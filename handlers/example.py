from flask_apidoc import ApiDoc
from flask_restful import Resource, marshal_with

from auth import token_auth
from base import resource_fields, APIResponse

class ExampleEndpoint(Resource):
    
    decorators = [marshal_with(resource_fields), token_auth.login_required]

    def get(self):
        return APIResponse(code=0)