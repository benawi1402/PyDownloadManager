import unittest
from config.Config import Config
import os
from os.path import exists
import pickle

from config.PickleConfigSource import PickleConfigSource


class TestPickleConfigSource(unittest.TestCase):
    def setUp(self):
        pickle_config_source = PickleConfigSource()
        os.remove(pickle_config_source.pickle_file)

    def test_save(self):
        pickle_config_source = PickleConfigSource()
        pickle_config_source.save()
        self.assertTrue(exists(pickle_config_source.pickle_file))
        with open(pickle_config_source.pickle_file, 'rb') as pickle_file_source:
            config = pickle.load(pickle_file_source)
        self.assertIsInstance(config, Config)

    def test_load(self):
        config = Config()

        pickle_config_source = PickleConfigSource()
        pickle_config_source.config = config
        pickle_config_source.save()

        loaded_config = pickle_config_source.load()
        self.assertEqual(config, loaded_config)
