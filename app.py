from flask import Flask
from router import register_urls

from database_client.db_init import db_init

app = Flask(__name__)
register_urls(app)
db_init()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
