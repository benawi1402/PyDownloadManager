import unittest
from config.Config import Config
import os
from os.path import exists
import yaml

from config.YAMLConfigSource import YAMLConfigSource


class TestPickleConfigSource(unittest.TestCase):
    def setUp(self):
        yaml_config_source = YAMLConfigSource()
        if exists(yaml_config_source.yaml_file_path):
            os.remove(yaml_config_source.yaml_file_path)

    def test_save(self):
        yaml_config_source = YAMLConfigSource()
        yaml_config_source.save()
        self.assertTrue(exists(yaml_config_source.yaml_file_path))
        with open(yaml_config_source.yaml_file_path, 'r') as yaml_file_source:
            config = yaml.load(yaml_file_source, Loader=yaml.UnsafeLoader)
        self.assertIsInstance(config, Config)

    def test_load(self):
        config = Config()

        yaml_config_source = YAMLConfigSource()
        yaml_config_source.config = config
        with open(yaml_config_source.yaml_file_path, 'x') as yaml_file_source:
            yaml.dump(yaml_config_source.config, yaml_file_source)

        loaded_config = yaml_config_source.load()
        self.assertIsInstance(loaded_config, Config)
        self.assertEqual(config, loaded_config)
