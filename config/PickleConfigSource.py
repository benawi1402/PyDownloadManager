import ConfigSource, Config
from os.path import exists
import pickle


class PickleConfigSource(ConfigSource):
    pickle_file = "config.pickle"

    def __init__(self):
        super().__init__()

    def initialize_source(self):
        if exists(self.pickle_file):
            self.config = pickle.load(open(self.pickle_file, 'rb'))
        else:
            pickle.dump(self.config, open(self.pickle_file, 'rb'))


