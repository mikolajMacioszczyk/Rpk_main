import json
from typing import Any

from flask import Flask, Response


def ok(flask_app: Flask, data: Any) -> Response:
    response = flask_app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


def bad_request(flask_app: Flask, message: str) -> Response:
    response = flask_app.response_class(
        response=json.dumps(message),
        status=400,
        mimetype='application/json'
    )
    return response


def internal_server_error(flask_app: Flask, message: str) -> Response:
    response = flask_app.response_class(
        response=json.dumps(message),
        status=500,
        mimetype='application/json'
    )
    return response
