from pyfakefs.fake_filesystem_unittest import TestCase

from config.Config import Config
from config.ConfigManager import ConfigManager
from config.PickleConfigSource import PickleConfigSource
from config.YAMLConfigSource import YAMLConfigSource


class TestConfigManager(TestCase):
    def setUp(self):
        self.setUpPyfakefs()

    def test_get_default_value(self):
        config_manager = ConfigManager()
        default_config = Config()
        for attr, value in default_config.__dict__.items():
            self.assertEqual(config_manager.get_default_value(attr), value)

    def test_refresh_sources(self):
        config_manager = ConfigManager()
        sources = {
            'pickle': PickleConfigSource(),
            'yaml': YAMLConfigSource(),
        }
        config_manager.source_objects = []
        config_manager.sources = sources
        config_manager.refresh_sources()
        for source_object in config_manager.source_objects:
            self.assertIsInstance(source_object, Config)

