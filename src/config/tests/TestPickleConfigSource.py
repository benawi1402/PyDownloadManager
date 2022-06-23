import os
import pickle
from os.path import exists

from pyfakefs.fake_filesystem_unittest import TestCase

from config.Config import Config
from config.PickleConfigSource import PickleConfigSource


class TestPickleConfigSource(TestCase):
    def setUp(self):
        self.setUpPyfakefs()
        pickle_config_source = PickleConfigSource()
        if exists(pickle_config_source.pickle_file_path):
            os.remove(pickle_config_source.pickle_file_path)

    def test_save(self):
        pickle_config_source = PickleConfigSource()
        pickle_config_source.save()
        self.assertTrue(exists(pickle_config_source.pickle_file_path))
        with open(pickle_config_source.pickle_file_path, 'rb') as pickle_file_source:
            config = pickle.load(pickle_file_source)
        self.assertIsInstance(config, Config)

    def test_load(self):
        config = Config()

        pickle_config_source = PickleConfigSource()
        pickle_config_source.config = config
        pickle_config_source.save()

        loaded_config = pickle_config_source.load()
        self.assertEqual(config, loaded_config)

    def test_exists(self):
        pickle_config_source = PickleConfigSource()
        pickle_config_source.save()

        self.assertTrue(pickle_config_source.exists())
