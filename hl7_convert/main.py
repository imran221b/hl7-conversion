#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hl7_convert.client import HL7Client
import click

@click.group()
@click.version_option()
def cli():
    """HL7 to JSON format converter"""
    pass

@cli.command()
@click.argument("input", nargs=1, type=click.File("r"))
@click.option("--output", "-o", type=click.File("w"), default=None, help="Output file path")
def tojson(input, output):
    """Convert given HL7 message to JSON format"""
    message = input.read()

    hl7_client = HL7Client()
    string_f = hl7_client.hl7tojsonconvert(message)

    if output:
        output.write(string_f + "\n")
    click.echo(string_f)

