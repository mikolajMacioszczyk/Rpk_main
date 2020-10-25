from flask import Flask

from exceptions.NotRegisteredException import NotRegisteredException
from models.AppConfiguration import AppConfiguration
from modules.di.modules_container import ModulesContainer
from modules.di.route_container import RouteContainer


class DiContainer:
    configuration: AppConfiguration = None
    modules_container: ModulesContainer = None
    route_container: RouteContainer = None
    flask_app: Flask = None

    def __del__(self):
        if self.modules_container is not None:
            del self.modules_container

    def register_configuration(self, configuration: AppConfiguration) -> None:
        self.configuration: AppConfiguration = configuration

    def register_modules(self) -> None:
        if self.configuration is None:
            raise NotRegisteredException(self.configuration)

        self.modules_container = ModulesContainer(self.configuration)
        self.modules_container.register()

    def register_endpoints(self, flask_app: Flask) -> None:
        if self.configuration is None:
            raise NotRegisteredException(self.configuration)

        self.route_container = RouteContainer(flask_app, self.configuration)
        self.route_container.register()
