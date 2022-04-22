#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from click.testing import CliRunner

from sample import cli


@pytest.fixture(scope="module")
def runner():
    """Pytest fixture for testing command line interfaces"""
    return CliRunner()


def test_sample_command_succeeds(runner):
    """Test fails if `sample print` does not succeed"""
    result = runner.invoke(cli, ["print"])
    assert result.exit_code == 0
