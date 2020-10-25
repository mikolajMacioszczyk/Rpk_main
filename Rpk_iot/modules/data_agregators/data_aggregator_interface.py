from abc import ABCMeta, abstractmethod
from typing import List

from models.AppConfiguration import AppConfiguration
from models.Sensors.Sensor import Sensor


class DataAggregatorInterface(metaclass=ABCMeta):
    configuration: AppConfiguration = None

    def __init__(self, configuration: AppConfiguration):
        self.configuration = configuration

    @abstractmethod
    def collect_data(self) -> List[Sensor]:
        ...
