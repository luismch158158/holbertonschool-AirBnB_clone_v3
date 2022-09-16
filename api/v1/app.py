#!/usr/bin/python3
"""Creating app with flask"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(self):
    """Close the SQLAlchemy session of the request or reload the json"""
    storage.close()


if (__name__ == "__main__"):
    ip = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')

    if (not ip):
        ip = '0.0.0.0'
    if (not port):
        port = '5000'

    app.run(host=ip, port=port, threaded=True)
