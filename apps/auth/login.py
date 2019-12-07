# coding: utf-8
import json
import datetime

from webargs.flaskparser import use_args
from marshmallow import fields
from database_client.redis_cli import redis_cli
from flask import make_response

from database_client.postgres import local_pg_cli
from werkzeug.security import check_password_hash
from apps.base_handler import BaseHandler
import random


class LoginHandler(BaseHandler):

    args_format = {
        'user_name': fields.Str(required=True, validate=bool),
        'password': fields.Str(required=True, validate=bool)
    }
    @use_args(args_format)
    def post(self, args):
        username = args['user_name']
        password = args['password']
        user_info = list(local_pg_cli.execute("SELECT * FROM www WHERE username='{}'".format(username)))
        if user_info:
            if check_password_hash(user_info[0][1], password):
                resp = self.write_response(status=1, data="/port")
                from flask import request
                origin = request.headers.get('Origin')
                resp.headers['Access-Control-Allow-Origin'] = origin
                resp.headers['Access-Control-Allow-Credentials'] = 'true'
                resp.headers['Access-Control-Allow-Methods'] = 'POST, GET,OPTIONS'
                resp.headers['Access-Control-Allow-Headers'] = \
                    'origin, x-csrftoken, Content-Type, accept, responseType, ' \
                    'x-requested-with'
                expire_time = datetime.datetime.now()+datetime.timedelta(days=7)
                resp.set_cookie('username', 'wgc1', expires=expire_time, domain='192.168.211.130:5000')
                return resp
            else:
                return self.write_response(status=0, err_msg="密码错误")
        else:
            return self.write_response(status=0, err_msg="用户不存在")
