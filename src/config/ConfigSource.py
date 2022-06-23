from abc import ABC, abstractmethod

from .Config import Config


class ConfigSource(ABC):
    config = Config()

    def supply_config(self):
        return self.config

    def refresh(self):
        if self.exists():
            self.config = self.load()
        else:
            self.save()

    def update(self, config: Config):
        self.config = config

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self, reload=False):
        pass

    @abstractmethod
    def exists(self):
        pass
