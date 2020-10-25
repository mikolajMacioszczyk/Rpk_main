import http.client
import json

from models.AppConfiguration import AppConfiguration
from models.Requests.RegisterNodeCommand import RegisterNodeCommand


class RegisterNoneClient:
    configuration: AppConfiguration = None

    def __init__(self, configuration: AppConfiguration):
        self.configuration = configuration
        self.client = http.client.HTTPConnection(self.configuration.server_address)

    def create_register_command(self):
        return RegisterNodeCommand(
            node_id=self.configuration.node_name,
            queue_channel=self.configuration.queue_channel)

    def register_me(self):
        headers = {'Content-type': 'application/json'}
        self.client.request('POST', '/api/register-node/register', self.create_register_command().to_json(), headers)

        response = self.client.getresponse()
        if response.getcode() != 202:
            raise Exception(response.read().decode())
