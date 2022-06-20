from config.YAMLConfigSource import YAMLConfigSource
from config.PickleConfigSource import PickleConfigSource
from config.Config import Config
from pydantic import ValidationError, validate_model


class ConfigManager:
    config_object = None
    default_config = Config()
    source_objects = []
    instance = None

    sources = {
        'pickle': PickleConfigSource(),
        'yaml': YAMLConfigSource(),
    }

    live_sources = ['pickle']

    def __init__(self):
        self.refresh_sources()
        self.refresh_config()

    def __new__(cls):
        if cls.instance is not None:
            return cls.instance
        else:
            inst = cls.instance = super(ConfigManager, cls).__new__()
            return inst

    def refresh_sources(self):
        self.source_objects = []
        for name, source in self.sources.items():
            source.refresh()
            self.source_objects.append(source.supply_config())

    def refresh_config(self):
        config_value_lock = []
        new_config = Config()
        for source_config in self.source_objects:
            for attr, value in source_config.__dict__.items():
                if value is not self.get_default_value(attr) and attr not in config_value_lock:
                    try:
                        setattr(new_config, attr, value)
                        config_value_lock.append(attr)
                    except ValidationError as e:
                        print(e.json)

        self.config_object = new_config

    def get_default_value(self, attr):
        return getattr(self.default_config, attr)

    def get_config(self, force_reload=False):
        if self.config_object.changed or force_reload:
            self.refresh_config()
        return self.config_object

    def persist(self):
        # re-validate just in case
        *_, validation_error = validate_model(self.config_object.__class__, self.config_object.__dict__)
        if validation_error:
            print('Config is invalid, not persisting')
            return
        for source in self.live_sources:
            self.sources[source].update()
            self.sources[source].save()
