from apps.base_handler import BaseHandler, login_required
from flask import make_response

import json
import datetime


class LogoutHandler(BaseHandler):
    #@login_required
    def post(self):
        resp = make_response(json.dumps({
            "status": 1,
            "data": "/login"
        }))
        resp.headers["Content-type"] = "application/json"
        resp.headers["status"] = 200
        from flask import request
        origin = request.headers.get('Origin')
        resp.headers['Access-Control-Allow-Origin'] = origin
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.headers['Access-Control-Allow-Methods'] = 'POST, GET,OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = \
            'origin, x-csrftoken, Content-Type, accept, responseType, ' \
            'x-requested-with'
        expire_time = datetime.datetime.now() + datetime.timedelta(days=7)
        #resp.set_cookie('username', 'wgc1', expires=expire_time)
        return resp
