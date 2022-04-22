#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click


@click.group()
def cli():
    """Sample CLI command group"""
    pass


@cli.command("print")
def sample_print():
    """Print a greeting message."""
    click.echo("Hello World!")
