#!/usr/bin/python3
"""route /status"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """"""
    obj_res = {
        "status": "OK"
    }

    return (jsonify(obj_res))
