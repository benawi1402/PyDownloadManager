from .ConfigSource import ConfigSource
from os.path import exists
import yaml


class YAMLConfigSource(ConfigSource):
    yaml_file_path = './config.yaml'

    def __init__(self):
        super().__init__()
        self.config = super().config

    def save(self):
        with open(self.yaml_file_path, 'x') as yaml_file:
            yaml.dump(self.config, yaml_file)

    def load(self):
        try:
            with open(self.yaml_file_path, 'r') as yaml_file:
                self.config = yaml.load(yaml_file, Loader=yaml.UnsafeLoader)
                return self.config
        except FileNotFoundError as e:
            print(e)

    def exists(self):
        return exists(self.yaml_file_path)
