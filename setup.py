#!/usr/bin/env python
# encoding: utf-8

"""Packaging script."""

import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
readme = open(os.path.join(here, 'README.rst')).read()

setup(
    name="circlify",
    description='Circle packing algorithm for Python',
    long_description=readme,
    long_description_content_type='text/x-rst',
    version="0.9.2",
    author="Elmotec",
    author_email="elmotec@gmx.com",
    license="MIT",
    keywords="circle packing enclosure hierarchy graph display visualization",
    url="http://github.com/elmotec/circlify",
    py_modules=['circlify'],
    test_suite='tests',
    setup_requires=[],
    tests_require=[],
    python_requires='>2.7,>=3.4',
    classifiers=["Development Status :: 4 - Beta",
                 "Operating System :: OS Independent",
                 "License :: OSI Approved :: MIT License",
                 "Natural Language :: English",
                 "Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 3.4",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 "Topic :: Software Development",
                 "Topic :: Utilities",
                 "Topic :: Scientific/Engineering :: Visualization",
                 "Intended Audience :: Developers",
                ],
)
