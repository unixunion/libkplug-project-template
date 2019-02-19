#!/usr/bin/env python

__author__ = 'keghol'

import argparse
import logging
import sys

# import libkplug before settings, but after logging
import libkplug
from libksettings import KSettings

# path modification to be able to run example against src, otherwise wont be able to resolve
# sys.path.insert(1, os.path.join(sys.path[0], '../src'))

# initialize the logger before kplug
logging.basicConfig(format='%(filename)s:%(lineno)s %(levelname)s %(message)s', stream=sys.stdout)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger().setLevel(logging.INFO)


def main():
    """
    The hello_world entrypoint

    :return:
    """
    logging.info("Starting up")

    parser = argparse.ArgumentParser(description='Hello World libkplug example project.')
    parser.add_argument('--config', type=str,
                        help='an integer for the accumulator')

    args = parser.parse_args()

    if not args.config:
        args.config = "config.yaml"

    # initialize settings with some default values
    settings = KSettings(config_filename=args.config,
                         MY_HELLO_WORLD_CLASS='HelloWorldPlugin',
                         PLUGINS=['hello_world.plugins.plugin_helloworld'])

    # get the class of the plugin
    clazz = libkplug.plugin_registry(settings.MY_HELLO_WORLD_CLASS)

    # instantiate it passing in the settings object
    inst = clazz(settings=settings)

    while True:
        try:
            pass
        except KeyboardInterrupt as e:
            logging.info("Terminating...")
            sys.exit(0)


if __name__ == "__main__":
    # execute only if run as a script
    main()
