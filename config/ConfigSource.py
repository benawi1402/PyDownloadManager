from abc import ABC, abstractmethod
from Config import Config


class ConfigSource(ABC):
    config = Config()

    def supply_config(self):
        return self.config

    @abstractmethod
    def initialize_source(self):
        pass
