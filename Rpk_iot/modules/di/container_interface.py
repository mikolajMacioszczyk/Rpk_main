from abc import ABCMeta, abstractmethod


class ContainerInterface(metaclass=ABCMeta):

    @abstractmethod
    def register(self):
        ...
