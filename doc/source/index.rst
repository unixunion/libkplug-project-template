.. libsolacev2 documentation master file, created by
   sphinx-quickstart on Thu Jan 10 13:46:01 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to libplug example plugin documentation!
================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

libkplug is a pluggable python development kit.

Testing
==================

pytest is used for this project, see https://docs.pytest.org/en/latest/goodpractices.html


Classes
==================

.. automodule:: hello_world
   :members:

.. autoclass:: hello_world.plugins.plugin_helloworld.HelloWorldPlugin(KPlugin)
  :special-members:
  :members:
  :private-members:
  :undoc-members:
  :show-inheritance:

.. automodule:: hello_world_binscripts.run
  :special-members:
  :members:
  :private-members:
  :undoc-members:
  :show-inheritance:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
