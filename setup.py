#!/usr/bin/env python
# setup
# Setup script for installing fastlife
#
# Author:   Benjamin Bengfort
# Created:  Sun Jul 26 08:38:29 2020 -0400
#
# Copyright (C) 2020 Bengfort.com
# For license information, see LICENSE
#
# ID: setup.py [] benjamin@bengfort.com $

"""
Setup script for installing fastlife.
See http://bbengfort.github.io/programmer/2016/01/20/packaging-with-pypi.html
"""

##########################################################################
## Imports
##########################################################################

import os
import codecs

from setuptools import setup
from setuptools import find_packages


##########################################################################
## Package Information
##########################################################################

## Basic information
NAME         = "fastlife"
DESCRIPTION  = "Benchmarks for implementations of Conway's Game of Life"
AUTHOR       = "Benjamin Bengfort"
EMAIL        = "benjamin@bengfort.com"
LICENSE      = "BSD 3-Clause"
REPOSITORY   = "https://github.com/bbengfort/fastlife"
PACKAGE      = "fastlife"
URL          = "https://fastlife.readthedocs.io/en/latest/"

## Define the keywords
KEYWORDS = [
    "cython",
    "game of life",
    "cellular automata",
    "parallel processing",
    "benchmarks",
]

## Define the classifiers
## See https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS  = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Topic :: Scientific/Engineering :: Artificial Life",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

## Important Paths
PROJECT = os.path.abspath(os.path.dirname(__file__))
REQUIRE_PATH = "requirements.txt"
VERSION_PATH = os.path.join(PACKAGE, "version.py")
PKG_DESCRIBE = "README.md"

## Directories to ignore in find_packages
EXCLUDES = (
    "tests", "tests.*",
    "bin",
    "docs", "docs.*",
    "fixtures",
    "register",
    "notebooks", "notebooks.*",
    "examples", "examples.*",
    "binder", "binder.*",
    "paper",
)

##########################################################################
## Helper Functions
##########################################################################


def read(*parts):
    """
    Assume UTF-8 encoding and return the contents of the file located at the
    absolute path from the REPOSITORY joined with *parts.
    """
    with codecs.open(os.path.join(PROJECT, *parts), "rb", "utf-8") as f:
        return f.read()


def get_version(path=VERSION_PATH):
    """
    Reads the python file defined in the VERSION_PATH to find the get_version
    function, and executes it to ensure that it is loaded correctly. Separating
    the version in this way ensures no additional code is executed.
    """
    namespace = {}
    exec(read(path), namespace)
    return namespace["get_version"](short=True)


def get_requires(path=REQUIRE_PATH):
    """
    Yields a generator of requirements as defined by the REQUIRE_PATH which
    should point to a requirements.txt output by `pip freeze`.
    """
    for line in read(path).splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            yield line


def get_description_type(path=PKG_DESCRIBE):
    """
    Returns the long_description_content_type based on the extension of the
    package describe path (e.g. .txt, .rst, or .md).
    """
    _, ext = os.path.splitext(path)
    return {".rst": "text/x-rst", ".txt": "text/plain", ".md": "text/markdown"}[ext]


##########################################################################
## Define the configuration
##########################################################################

config = {
    "name": NAME,
    "version": get_version(),
    "description": DESCRIPTION,
    "long_description": read(PKG_DESCRIBE),
    "long_description_content_type": get_description_type(PKG_DESCRIBE),
    "classifiers": CLASSIFIERS,
    "keywords": KEYWORDS,
    "license": LICENSE,
    "author": AUTHOR,
    "author_email": EMAIL,
    "url": URL,
    "project_urls": {
        "Documentation": URL,
        "Download": "{}/tarball/v{}".format(REPOSITORY, get_version()),
        "Source": REPOSITORY,
        "Tracker": "{}/issues".format(REPOSITORY),
    },
    "download_url": "{}/tarball/v{}".format(REPOSITORY, get_version()),
    "packages": find_packages(where=PROJECT, exclude=EXCLUDES),
    "package_data": {},
    "zip_safe": False,
    "entry_points": {
        "console_scripts": [
            "fastlife = fastlife.__main__:main"
        ],
    },
    "install_requires": list(get_requires()),
    "python_requires": ">=3.4, <4",
    "setup_requires": ["pytest-runner"],
    "tests_require": ["pytest"],
}


##########################################################################
## Run setup script
##########################################################################

if __name__ == "__main__":
    setup(**config)
