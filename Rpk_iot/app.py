import asyncio
import sys
from asyncio import AbstractEventLoop

from flask import Flask

from models.AppConfiguration import AppConfiguration
from modules.di.di_container_module import DiContainer
from modules.generators import uuid_generator_module

di_container: DiContainer = DiContainer()

def main():
    app_configuration: AppConfiguration = AppConfiguration(
        node_name="pi_node",
        queue_host="localhost",
        queue_channel=uuid_generator_module.new_guid(),
        server_address="localhost:5000")
    app = Flask(__name__)

    di_container.register_configuration(app_configuration)
    di_container.register_modules()
    di_container.register_endpoints(app)

    di_container.modules_container.http_client.register_me()
    di_container.modules_container.data_worker.create_worker()

    app.run(host='127.0.0.1', port=21037)


def close_app():
    if di_container is not None:
        del di_container
        sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        close_app()
    except:
        close_app()
