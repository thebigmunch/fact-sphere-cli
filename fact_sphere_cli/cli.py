import sys

import click
import fact_sphere
from click_default_group import DefaultGroup

from . import __title__, __version__

CONTEXT_SETTINGS = dict(max_content_width=200, help_option_names=['-h', '--help'])


@click.group(cls=DefaultGroup, default='text', default_if_no_args=True, context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__, '-V', '--version', prog_name=__title__, message="%(prog)s %(version)s")
def fact_sphere_cli():
	"""A CLI for Portal 2 Fact Sphere facts."""

	pass


@fact_sphere_cli.command()
@click.version_option(__version__, '-V', '--version', prog_name=__title__, message="%(prog)s %(version)s")
@click.option('--read', is_flag=True, default=False, help="Return contents for piping.")
def audio(read):
	"""Get the filepath or file content for a random fact."""

	f = fact_sphere.api.audio()

	if not read:
		click.echo(f"Audio: {f.filepath}")
	else:
		sys.stdout.buffer.write(f.read())


@fact_sphere_cli.command()
@click.version_option(__version__, '-V', '--version', prog_name=__title__, message="%(prog)s %(version)s")
def fact():
	"""Get the text, filepath, and type for a random fact."""

	f = fact_sphere.api.fact()

	click.echo(f"Text: {f.text}")
	click.echo(f"Audio: {f.audio.filepath}")
	click.echo(f"Type: {f.type.value}")


@fact_sphere_cli.command()
@click.version_option(__version__, '-V', '--version', prog_name=__title__, message="%(prog)s %(version)s")
def text():
	"""Get the text for a random fact."""

	click.echo(fact_sphere.api.fact().text)
