#!/usr/bin/env python
import os
import re

from setuptools import setup, find_packages


setup(
    name="aeso-python-api",
    version="0.0.1",
    description="A Python API for Aeso Data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Guanjie Shen",
    url="https://github.com/guanjieshen/aeso-python-api",
    packages=find_packages(exclude=["tests*"]),
    install_requires=["requests>=2.5.0,<3.0.0"],
    license="MIT License",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
)
