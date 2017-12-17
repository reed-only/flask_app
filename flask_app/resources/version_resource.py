"""
Version API
"""

from flask import jsonify

from flask_app.extensions import app

API_VERSION = '0.1'


@app.route('/version')
def get_version():
    """
    Return API version
    """
    return jsonify(version=API_VERSION)
