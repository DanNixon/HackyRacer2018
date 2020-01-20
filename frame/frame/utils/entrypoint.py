import click

import solid as sp


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.pass_context
def scad(ctx):
    click.echo(sp.scad_render(ctx.obj))


@cli.command()
def bom():
    import frame
    frame.utils.bom.pretty_print()


def main(thing):
    cli(obj=thing)
