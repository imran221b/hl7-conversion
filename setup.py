#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="hl7-hl7_convert",
    version="0.1.1",
    author="Imran Hasan",
    author_email="imran221b@gmail.com",
    description="Package to hl7_convert HL7 messages to JSON format",
    url="",
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
