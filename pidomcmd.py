#!/usr/bin/python

import click
import importlib
import os
import types

from pidomctrl import PidomCtrl

# Get config file from env and read in dict (as Flask does)
settings_file = os.environ['SETTINGS']
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
filename = os.path.join(dir_path, settings_file)
config = {}
with open(filename, mode='rb') as config_file:
    exec(compile(config_file.read(), filename, 'exec'), config)

pidomCtrl = PidomCtrl(config['SWITCHES'], config['PERSISTENT_STATE'], config['REDIS_HOST'], config['REDIS_PORT'], config['REDIS_DB'], config['REDIS_PASSWORD'])

@click.group()
def cli():
    pass

@click.command()
@click.option('--light', help='Light id to toggle', type=click.Choice(
    ['alloff', 'outside', 'stairs', 'frontdoorgroupoff', 'frontdoorgroupon']))
def toggle(light_id):
    """Toggle light based on id"""
    if light_id == "alloff":
        pidomCtrl.pulse("alloff")
    elif light_id == "outside":
        pidomCtrl.pulse("outside")
    elif light_id == "stairs":
        pidomCtrl.pulse("stairs")
    elif light_id == "frontdoorgroupoff":
        pidomCtrl.pulse("persistedoff")
    elif light_id == "persistedon":
        pidomCtrl.pulse("frontdoorgroupon")

@click.command()
def garage():
    """Garage switch"""
    pidomCtrl.pulse('garage', 1)

@click.command()
@click.option('--direction', help='Direction movement screen', type=click.Choice(['up', 'down']))
def screen(direction):
    """Move screen up or down"""
    pidomCtrl.pulse('screen_{}'.format(direction))

@click.command()
@click.option('--set', help='Set state tuple (outside, stairs)', type=(bool, bool), default=(False,False))
@click.option('--get', help='Get State tuple (outside, stairs)', is_flag=True, default=False)
def frontdoorgroupstate(get, set):
    "Get or set light state outside and stairs"
    if get:
        click.echo(pidomCtrl.getState())
    else:
        click.echo(pidomCtrl.setState(set))

cli.add_command(toggle)
cli.add_command(garage)
cli.add_command(screen)
cli.add_command(frontdoorgroupstate)

if __name__ == '__main__':
    cli()
