import ConfigSource
from os.path import exists
import pickle


class PickleConfigSource(ConfigSource):
    pickle_file = "config.pickle"

    def __init__(self):
        super().__init__()
        self.config = super().config

    def save(self):
        return pickle.dump(self.config, open(self.pickle_file, 'rb'))

    def load(self):
        return pickle.load(open(self.pickle_file, 'rb'))

    def exists(self):
        return exists(self.pickle_file)
