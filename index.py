import json
from flask import Flask, request
from flask_restful import Resource
from api import api
from flask_script import Manager
from flask_apidoc import ApiDoc
from flask_apidoc.commands import GenerateApiDoc

from models import db
# from utils.sentry import sentry
from utils.response import MESSAGE


app = Flask(__name__)
# sentry.init_app(app)
api.init_app(app)
doc = ApiDoc(app=app)
manager = Manager(app)
manager.add_command('apidoc', GenerateApiDoc())

@app.before_request
def _db_connect():
    if db.is_closed():
        db.connect()

@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

@app.after_request
def after_request(response):
    # try:
    #     r = response.response[0].decode("utf-8")
    #     r = json.loads(r)
    #     if r.get("code") != 0:
    #         sentry.captureMessage("{}".format(MESSAGE.get(r.get("code"))), extra={"Request":request.__dict__, "Response":response.__dict__})
    # except Exception as e:
    #     print(e)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    # app.run(host="0.0.0.0", debug=True, port=PORT)
    # manager.run(host="0.0.0.0", debug=True, port=PORT)
    manager.run()
    