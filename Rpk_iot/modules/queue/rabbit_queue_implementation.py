import pika
from pika import BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel

from models.AppConfiguration import AppConfiguration
from modules.queue.queue_inteface import QueueInterface


class RabbitQueue(QueueInterface):

    connection: BlockingConnection = None
    channel: BlockingChannel = None

    def __init__(self, configuration: AppConfiguration):
        super().__init__(configuration)
        self.register()

    def __del__(self):
        if self.channel is not None:
            self.connection.close()
        super().__del__()

    def register(self) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.configuration.queue_host))
        self.channel: BlockingChannel = self.connection.channel()

        self.channel.queue_declare(self.configuration.queue_channel)

    def send(self, bytes_message: bytes) -> None:
        self.channel.basic_publish(exchange='', routing_key=self.configuration.queue_channel, body=bytes_message)
