from YAMLConfigSource import YAMLConfigSource
from PickleConfigSource import PickleConfigSource
from Config import Config

config_object = None
default_config = Config()
source_objects = []

sources = {
    'pickle': PickleConfigSource(),
    'yaml': YAMLConfigSource(),
}


def init_sources():
    global source_objects
    global sources
    for name, source in sources.items():
        source.initialize_source()
        source_objects.append(source.supply_config())


def get_config():
    global config_object
    global source_objects
    if config_object is None:
        config_value_lock = []
        new_config = Config()
        for source_config in source_objects:
            for attr, value in source_config.__dict__.items():
                if value is not get_default_value(attr) and attr not in config_value_lock:
                    setattr(new_config, attr, value)
                    config_value_lock.append(attr)

        config_object = new_config

    return config_object


def get_default_value(attr):
    global default_config
    return getattr(default_config, attr)


init_sources()
