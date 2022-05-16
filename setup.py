#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
README = (HERE / "README.md").read_text()

setup(
    name="hl7-conversion",
    version="0.1.1",
    author="Imran Hasan",
    author_email="imran221b@gmail.com",
    description="Package to convert HL7 messages to JSON format",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/imran221b/hl7-conversion",
    packages=find_packages(exclude=["docs", "tests"]),
    platforms=["posix"],
    entry_points={
        "console_scripts": [
            "hl7 = hl7_convert.main:cli",
        ],
    },
    install_requires=[
        "Click",
        "hl7apy"
    ],
    extras_require={
        "test": [
            "pytest",
        ],
        "dev": [
            "black",
        ],
    },
)
