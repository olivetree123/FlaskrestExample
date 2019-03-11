from flask_apidoc import ApiDoc
from flask_restful import Resource, marshal_with

from auth import token_auth
from models.example import Example
from base import resource_fields, APIResponse
from utils.response import BAD_REQUEST, OBJECT_NOT_FOUND, WRITE_DATA_FAILED, INVALID_DATA

class ExampleEndpoint(Resource):
    
    decorators = [marshal_with(resource_fields), token_auth.login_required]
    Model = Example

    def get(self, uid):
        """
        @api {GET} /api/example/<uid> 获取Example
        @apiName GetExample
        @apiGroup Example

        @apiExample 返回值
        {
            "code": 0,
            "message": null,
            "data": null
        }
        """
        r = self.Model.get_with_uid(uid)
        return APIResponse(data=r)

    
    def post(self):
        """
        @api {POST} /api/example 创建Example
        @apiName CreateExample
        @apiGroup Example

        @apiExample 参数
        {
            "title":"123",
        }

        @apiExample 返回值
        {
            "code": 0,
            "message": null,
            "data": null
        }
        """
        params = request.get_json()
        if not params:
            return APIResponse(code=BAD_REQUEST)
        status = self.Model.verify_params(**params)
        if not status:
            return APIResponse(code=BAD_REQUEST)
        status = self.Model.validate(**params)
        if not status:
            return APIResponse(code=INVALID_DATA)
        r = self.Model.create_data(**params)
        if not r:
            return APIResponse(code=WRITE_DATA_FAILED)
        return APIResponse(data=r)
    
    def put(self, uid):
        """
        @api {PUT} /api/example/<uid> 更新Example
        @apiName UpdateExample
        @apiGroup Example

        @apiExample 参数
        {
            "uid":"9d404a96cb664023ac0379d87a1a53c9",
            "title":"123",
        }

        @apiExample 返回值
        {
            "code": 0,
            "message": null,
            "data": null
        }
        """
        params = request.get_json()
        if not params:
            return APIResponse(code=BAD_REQUEST)
        status = self.Model.verify_params(**params)
        if not status:
            return APIResponse(code=BAD_REQUEST)
        r = self.Model.update_by_uid(uid, **params)
        if not r:
            return APIResponse(code=OBJECT_NOT_FOUND)
        return APIResponse(data=r)
    
    def delete(self, uid):
        """
        @api {DELETE} /api/example/<uid> 删除Example
        @apiName DeleteExample
        @apiGroup Example

        @apiExample 返回值
        {
            "code": 0,
            "message": null,
            "data":null
        }
        """
        r = self.Model.remove(uid)
        if not r:
            return APIResponse(code=OBJECT_NOT_FOUND)
        return APIResponse()