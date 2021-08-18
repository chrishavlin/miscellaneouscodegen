"""Console script for miscellaneouscodegen."""
import sys
import click
from miscellaneouscodegen import template_registry

@click.group()
def main():
    pass

@main.command()
@click.argument('filename')
@click.option(
    "--template_type",
    default="dask_reductions",
    help="the available generative templates",
)
@click.option(
    "--header",
    default=None,
    help="header text for output file",
)
def generate(filename, template_type, header):
    if template_type in template_registry.keys():
        for temp_obj in template_registry[template_type]:
            temp_obj().write(filename, header)
        print(f"wrote reductions to {filename}")
    else:
        raise ValueError("template_type must be a registered template")

@main.command()
def list_templates():
    print(f"registered templates: {list(template_registry.keys())}")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
