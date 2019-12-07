# coding: utf-8

from webargs.flaskparser import use_args
from marshmallow import fields

from werkzeug.security import generate_password_hash

from apps.base_handler import BaseHandler
from database_client.postgres import local_pg_cli


class RegisterHandler(BaseHandler):

    args_format = {
        'user_name': fields.Str(required=True, validate=bool),
        'password': fields.Str(required=True, validate=bool),
        're_password': fields.Str(required=True, validate=bool),
        'email': fields.Email(required=False, validate=bool),
        'area': fields.Str(required=False, validate=bool)
    }

    @use_args(args_format)
    def post(self, args):
        try:
            username = args['user_name']
            password = args['password']
            re_password = args['re_password']
            if password != re_password:
                return self.write_response(status=0, err_msg='两次密码不一致',
                                           err_code=1202)

            userinfo = local_pg_cli.execute("SELECT * FROM www WHERE username='{}'".format(username))
            result = list(userinfo)
            if result:
                return self.write_response(err_msg="该用户已经存在")

            local_pg_cli.execute("INSERT INTO www (username, password) VALUES ('{}', '{}')".format(username,generate_password_hash(password)))
            return self.write_response()

        except Exception as e:
            import traceback
            traceback.print_exc()

    def get(self):
        return self.write_response(
            status=2
        )
