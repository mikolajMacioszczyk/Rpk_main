import asyncio
import threading
from asyncio import AbstractEventLoop
import time
from typing import List

from models.Sensors.Sensor import Sensor
from modules.converteres import byte_converter
from modules.data_agregators.data_aggregator_interface import DataAggregatorInterface
from modules.queue.queue_inteface import QueueInterface


class SensorDataSender:
    queue: QueueInterface = None
    data_aggregator: DataAggregatorInterface = None
    loop: threading.Thread = None

    is_running: bool = False

    def __init__(self, queue: QueueInterface, data_aggregator: DataAggregatorInterface):
        self.queue = queue
        self.data_aggregator = data_aggregator

    def __del__(self):
        self.is_running = False
        if self.loop is not None:
            self.loop.join()

    def create_worker(self):
        self.is_running = True
        self.loop = threading.Thread(target=self.process_data)
        self.loop.start()
        # self.loop = asyncio.get_running_loop()
        # self.loop.create_task(self.process_data())
        # self.loop.run_forever()

    def process_data(self):
        while True:
            data: List[Sensor] = self.data_aggregator.collect_data()
            for item in data:
                byte_sensor_data = byte_converter.to_bytes(item.to_json())
                self.queue.send(byte_sensor_data)
            time.sleep(5)
