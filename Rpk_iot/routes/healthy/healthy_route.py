from flask import Flask

from models.AppConfiguration import AppConfiguration
from routes.base_routes import ok


class HealthyRoute:
    flask_app: Flask = None
    configuration: AppConfiguration = None

    def __init__(self, flask_app: Flask, configuration: AppConfiguration):
        self.flask_app: Flask = flask_app
        self.configuration = configuration

    def register_endpoints(self):
        print("register healthy endpoints")

        @self.flask_app.route('/healthy', methods=['GET'])
        def healthy():
            """ Returning healthy status."""
            return ok(self.flask_app, self.configuration.to_json())
