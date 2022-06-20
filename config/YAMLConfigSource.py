import ConfigSource
from os.path import exists
import yaml

class YAMLConfigSource(ConfigSource):
    yaml_file = 'config.yaml'

    def __init__(self):
        super().__init__()

    def initialize_source(self):
        if exists(self.yaml_file):
            self.config = yaml.load(open(self.yaml_file, 'rb'), Loader=yaml.Loader)
        else:
            yaml.dump(self.config, open(self.yaml_file, 'rb'))