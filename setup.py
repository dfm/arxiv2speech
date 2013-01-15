#!/usr/bin/env python

import os
import sys
from setuptools import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

setup(
    name="arxiv2speech",
    version="0.0.2",
    description="Convert the current abstracts listed on the arxiv to a set "
                "of audio files.",
    long_description=open("README.rst").read(),
    author="Dan Foreman-Mackey",
    author_email="danfm@nyu.edu",
    url="https://github.com/dfm/arxiv2speech",
    py_modules=["arxiv2speech"],
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    scripts=["scripts/arxiv2speech"],
    install_requires=["html2text", "docopt", "feedparser"],
    classifiers=(
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ),
)
