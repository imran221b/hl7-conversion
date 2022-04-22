#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest

from hl7_convert.client import HL7Client

@pytest.fixture(scope="module")
def client():
    """ Pytest fixture for providing HL7Client instance """
    return HL7Client()
