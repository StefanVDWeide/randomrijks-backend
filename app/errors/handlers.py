from app import db
from app.errors import bp
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


# A catch all function which returns the error code and message back to the user
def error_response(status_code, message=None):
    payload = {"error": HTTP_STATUS_CODES.get(status_code, "Unknown error")}
    if message:
        payload["msg"] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


# Returns a 400 error code when a bad request has been made
def bad_request(message):
    return error_response(400, message)


@bp.app_errorhandler(404)
def not_found_error(error):
    """
    Flask error handler that catches 404 errors and sends a JSON error response
    Parameters
    ----------
    error
        The error object generate by Flask
    Returns
    -------
        Calls the error response function to return a JSON object to the front-end
    """
    return error_response(404, "Not Found")


# Flask error handler that catches 500 errors, rolls back the db session and sends a JSON error response
@bp.app_errorhandler(500)
def internal_error(error):
    """
    Flask error handler that catches 500 errors and sends a JSON error response
    Parameters
    ----------
    error
        The error object generate by Flask
    Returns
    -------
        Calls the error response function to return a JSON object to the front-end
    """
    db.session.rollback()
    return error_response(500, "Internal Server Error")
