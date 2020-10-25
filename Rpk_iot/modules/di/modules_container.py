from models.AppConfiguration import AppConfiguration
from modules.data_agregators.data_aggregator_interface import DataAggregatorInterface
from modules.data_agregators.data_aggregator_virtualization import DataAggregatorVirtualization
from modules.di.container_interface import ContainerInterface
from modules.http_clients.register_node_client import RegisterNoneClient
from modules.queue.queue_inteface import QueueInterface
from modules.queue.rabbit_queue_implementation import RabbitQueue
from modules.workers.sensor_data_sender import SensorDataSender


class ModulesContainer(ContainerInterface):
    configuration: AppConfiguration = None
    data_aggregator: DataAggregatorInterface = None
    queue: QueueInterface = None
    http_client: RegisterNoneClient = None

    data_worker: SensorDataSender = None

    def __init__(self, configuration: AppConfiguration):
        self.configuration = configuration

    def __del__(self):
        del self.data_worker
        del self.queue

    def register(self):
        self.http_client = RegisterNoneClient(self.configuration)
        self.data_aggregator = DataAggregatorVirtualization(self.configuration)
        self.queue = RabbitQueue(self.configuration)

        self.data_worker = SensorDataSender(self.queue, self.data_aggregator)

