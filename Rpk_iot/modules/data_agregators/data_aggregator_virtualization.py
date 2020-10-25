from datetime import datetime
from typing import List

from models.AppConfiguration import AppConfiguration
from models.Sensors.Sensor import Sensor
from modules.data_agregators.data_aggregator_interface import DataAggregatorInterface
from modules.generators import uuid_generator_module


class DataAggregatorVirtualization(DataAggregatorInterface):

    def __init__(self, configuration: AppConfiguration):
        super().__init__(configuration)

    def collect_data(self) -> List[Sensor]:
        sensor_data: List[Sensor] = []
        for item in range(10):
            sensor = Sensor(sensor_id=uuid_generator_module.new_guid(),
                            node_id=self.configuration.node_name,
                            measurement_time=datetime.utcnow(),
                            sensor_value=float(1+item),
                            localization=item % 5,
                            sensor_type=0,
                            sensor_group_guid=uuid_generator_module.new_guid())
            sensor_data.append(sensor)

        sensor = Sensor(sensor_id=uuid_generator_module.new_guid(),
                        node_id=self.configuration.node_name,
                        measurement_time=datetime.utcnow(),
                        sensor_value=float(0.4),
                        localization=0,
                        sensor_type=1,
                        sensor_group_guid=uuid_generator_module.new_guid())
        sensor_data.append(sensor)

        return sensor_data
