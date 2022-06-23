import pickle
from os.path import exists

from exception.ConfigPersistenceError import ConfigPersistenceError
from .ConfigSource import ConfigSource


class PickleConfigSource(ConfigSource):
    pickle_file_path = "./config.pickle"

    def __init__(self):
        super().__init__()
        self.config = super().config

    def save(self):
        with open(self.pickle_file_path, 'xb') as pickle_file:
            pickle.dump(self.config, pickle_file)

    def load(self, reload=False):
        try:
            with open(self.pickle_file_path, 'rb') as pickle_file:
                self.config = pickle.load(pickle_file)
                return self.config
        except FileNotFoundError as e:
            if reload:
                raise ConfigPersistenceError(f'Failed to persist configuration file at {self.pickle_file_path}', e)
            else:
                self.save()
                return self.load(True)

    def exists(self):
        return exists(self.pickle_file_path)
