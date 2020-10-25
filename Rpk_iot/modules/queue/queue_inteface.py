from abc import ABCMeta, abstractmethod

from models.AppConfiguration import AppConfiguration


class QueueInterface(metaclass=ABCMeta):
    configuration: AppConfiguration = None

    def __init__(self, configuration: AppConfiguration):
        self.configuration = configuration
        print("Connect to queue.")

    def __del__(self):
        print("Disconnect from queue.")

    @abstractmethod
    def send(self, bytes_message: bytes):
        ...
