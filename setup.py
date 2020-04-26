import os
import io

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="markopolo",
    version="2020.04.26",
    description="Markup Language Parser",
    long_description=long_description,
    author="Raja Simon",
    url="https://github.com/hackerassist/markopolo",
    python_requires=">=3.6.0",
    py_modules=["markopolo"],
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
