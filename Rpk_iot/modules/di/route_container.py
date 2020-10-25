from flask import Flask

from models.AppConfiguration import AppConfiguration
from modules.di.container_interface import ContainerInterface
from routes.healthy.healthy_route import HealthyRoute


class RouteContainer(ContainerInterface):
    healthy_route: HealthyRoute = None

    def __init__(self, flask_app: Flask, configuration: AppConfiguration):
        self.configuration = configuration
        self.flask_app = flask_app

    def register(self):
        self.create_healthy_route()

    def create_healthy_route(self):
        self.healthy_route: HealthyRoute = HealthyRoute(self.flask_app, self.configuration)
        self.healthy_route.register_endpoints()
