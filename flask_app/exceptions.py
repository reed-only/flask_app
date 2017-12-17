"""
Error handlers
"""

from flask import jsonify

from flask_app.extensions import app


class ApiError(Exception):
    """
    Generic API error.  Extend this class for specific API errors.
    """
    def __init__(self, message, status_code):
        super().__init__()
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return 'ApiError(type={}, status_code={}, message="{}")'.format(self.__class__.__name__, self.status_code,
                                                                        self.message)


class BadRequest(ApiError):
    """
    Bad request exception
    """
    def __init__(self, message):
        super().__init__(message, status_code=400)


class ServerError(ApiError):
    """
    Server error exception
    """
    def __init__(self, message):
        super().__init__(message, status_code=500)


@app.errorhandler(ApiError)
def respond_api_error(error):
    """
    Log API error and return response
    """
    app.logger.error(str(error))
    response = jsonify(message=error.message, status_code=error.status_code)
    response.status_code = error.status_code
    return response
