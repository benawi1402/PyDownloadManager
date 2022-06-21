from .ConfigSource import ConfigSource
from os.path import exists
import pickle


class PickleConfigSource(ConfigSource):
    pickle_file = "./config.pickle"

    def __init__(self):
        super().__init__()
        self.config = super().config

    def save(self):
        with open(self.pickle_file, 'xb') as pickle_file:
            pickle.dump(self.config, pickle_file)

    def load(self):
        try:
            with open(self.pickle_file, 'rb') as pickle_file:
                self.config = pickle.load(pickle_file)
                return self.config
        except FileNotFoundError as e:
            print(e)

    def exists(self):
        return exists(self.pickle_file)
