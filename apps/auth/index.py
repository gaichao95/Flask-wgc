from flask import render_template

from apps.base_handler import BaseHandler
from database_client.postgres import pg_cli


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        return render_template('index.html')

