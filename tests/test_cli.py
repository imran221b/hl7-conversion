#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from click.testing import CliRunner

from hl7_convert.main import cli

@pytest.fixture(scope="module")
def runner():
    """Pytest fixture for testing command line interfaces"""
    return CliRunner()

def test_json_generated(runner):
    """Test fails if json could not be generated from the given input hl7 message"""
    result = runner.invoke(cli, ["tojson", "input.txt", "-o", "output.txt"])
    assert result.exit_code == 0
    assert "output.txt" in result.output