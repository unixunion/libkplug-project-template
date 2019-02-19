# libkplug project template

This is a simple template for [libkplug](https://github.com/unixunion/libkplug) based modular applications.

## src/

Contains the source top level modules, and "binscripts" which are mapped to shell commands in setup.py

## config.yaml

The libkplug/libksettings example yaml config'. It declares which plugins to load, along with any other generic 
key:value properties required by the application.

## dev run

    python ./src/hello_world_binscripts/run.py --config config.yaml
    
# install

    python setup.py install
    
# installed entrypoints

Setup.py is used to create shell scripts and other entrypoints from modules. See setup.py for details.

    hello_world
    
# docs

    pip install sphinx_rtd_theme
    make html