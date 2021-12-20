from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def listen(self, commands):
        pass

    @abstractmethod
    def get_command(self):
        pass

    @abstractmethod
    def get_args(self):
        pass

    @abstractmethod
    def execute(self):
        pass
