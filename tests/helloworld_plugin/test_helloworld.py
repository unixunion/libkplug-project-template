__author__ = 'keghol'

import os
import sys
import logging
from libkplug import KPlugin
from libksettings import KSettings
import pytest

logging.basicConfig(level=logging.WARN,
                    format='%(module)s %(filename)s:%(lineno)d %(asctime)s %(levelname)s %(message)s',
                    stream=sys.stdout)
logging.getLogger().setLevel(logging.INFO)

sys.path.insert(1, os.path.join(sys.path[0], '../../src'))

import hello_world

class TestClass(object):

    @pytest.fixture(autouse=True)
    def test_setup(self):
        # instantiate a settings, and a registry from the libkplug project
        self.settings = KSettings(config_filename="tests/test_config.yaml")
        self.registry = KPlugin()

    def test_hello_static_method(self):
        # in test_config.yaml, we have set MY_HELLO_WORLD_CLASS, lets use that to identify the plugin
        t = self.registry(self.settings.MY_HELLO_WORLD_CLASS).hello_world()
        assert t == "Hello World"

    @pytest.mark.timeout(10, "slow", method="thread")
    def test_run_class(self):
        clazz = self.registry(self.settings.MY_HELLO_WORLD_CLASS)

        # instantiate it passing in the settings object
        inst: hello_world.plugins.plugin_helloworld.HelloWorldPlugin = clazz(settings=self.settings)
        while inst.get_timestamp_count() < 2:
            pass

        assert inst.get_timestamp_count() > 1