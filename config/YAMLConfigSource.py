import ConfigSource
import yaml


class YAMLConfigSource(ConfigSource):
    yaml_file = 'config.yaml'

    def __init__(self):
        super().__init__()
        self.config = super().config

    def save(self):
        yaml.dump(self.config, open(self.yaml_file, 'rb'))

    def load(self):
        self.config = yaml.load(open(self.yaml_file, 'rb'), Loader=yaml.Loader)
