"""
Start the flask app
"""

from flask_app.extensions import app

if __name__ == '__main__':
    app.run(host='0.0.0.0')
