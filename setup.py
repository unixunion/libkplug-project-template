"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name='libkplug-template',
    version='0.0.1',
    description='A sample libkplug project',
    long_description_content_type='text/markdown',
    url='https://github.com/unixunion/libkplug-template',
    author='Kegan Holtzhausen',
    author_email='marzubus@gmail.com',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ],
    keywords='sample setuptools development',  # Optional
    package_dir={'': 'src'},
    packages=[
        'hello_world',
        'hello_world.plugins',
        'hello_world_binscripts'
    ],
    entry_points = {
        'console_scripts': [
            # this creates a "hello_world" script off the "main" method in run.py under src/hello_world_binscripts
            'hello_world = hello_world_binscripts.run:main']
    },
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    install_requires=['libkplug'],
    tests_require=['libkplug', 'pytest'],
    setup_requires=['pytest-runner'],
    #test_suite="test.testrunner.testsuite",
    dependency_links=['git+https://github.com/unixunion/libkplug.git@0.2.5#egg=libkplug-0.2.5'],
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/unixunion/libkplug-template/issues',
        'Source': 'https://github.com/unixunion/libkplug-template',
    },
)