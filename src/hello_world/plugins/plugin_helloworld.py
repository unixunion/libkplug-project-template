__author__ = 'keghol'

import logging
import _thread
import time

# initializes the plugin system
import libkplug
from libkplug import KPlugin


# a inline plugin registration
@libkplug.plugin_registry.register
class HelloWorldPlugin(KPlugin):
    """
    A simple example KPlugin that starts two threads which print the time.
    """
    plugin_name = 'HelloWorldPlugin'

    timestamp_count = 0

    def __init__(self, *args, **kwargs):
        """
        Instantiate

        :param args:
        :param kwargs:
        """
        logging.info('Instantiating instance of: %s args: %s and kwargs: %s' % (self.plugin_name, args, kwargs))
        # Create two threads as follows
        try:
            _thread.start_new_thread(self.print_time, ("Thread-1", 2,))
            _thread.start_new_thread(self.print_time, ("Thread-2", 4,))
        except:
            logging.error("Error: unable to start thread")

    def hello(self, name="default"):
        """
        Example of a instance method

        :param name:
        :returns: None
        :rtype: None
        """
        logging.info("Hello %s from %s instance method" % (name, self))
        return name

    @staticmethod
    def hello_world():
        """
        Static method example

        :returns: "hello world"
        :rtype: str
        """
        logging.info("Hello World")
        return "Hello World"

    def print_time(self, thread_name, delay):
        """
        Prints the time via logging system

        :param thread_name: The name of the thread
        :param delay: milliseconds between log events
        :return: None
        """
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            self.timestamp_count += 1
            logging.info("%s: %s: %s" % (self, thread_name, time.ctime(time.time())))

    def get_timestamp_count(self):
        return self.timestamp_count