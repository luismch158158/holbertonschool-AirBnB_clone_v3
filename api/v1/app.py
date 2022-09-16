#!/usr/bin/python3
"""Creating app with flask"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import jsonify

app = Flask(__name__)

app.register_blueprint(app_views)

@app.errorhandler(404)
def not_found(error):
    """This method return a JSON response in case throw error 404"""
    return jsonify({"error": "Not found"})

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

    app.run(host=ip, port=port, threaded=True, debug=True)
