# SPDX-FileCopyrightText: 2025-present kc3zvd <aaron@kc3zvd.net>
#
# SPDX-License-Identifier: MIT
import click

from paperless_ngx_llamaindex.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="paperless-ngx-llamaindex")
def paperless_ngx_llamaindex():
    click.echo("Hello world!")
