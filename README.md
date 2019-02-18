# libkplug project template

## src/

Contains the source top level modules, and "binscripts" which are mapped to shell commands in setup.py

## config.yaml

The libkplug / libksettings example yaml config is loaded from the 'cwd'. It declares which plugins to load,
along with any other generic key:value properties required by the application.

## dev run

    python ./src/hello_world_binscripts/run.py --config config.yaml
    
# install

    python setup.py install
    
# installed run

    hello_world