"""Top-level package for miscellaneouscodegen."""

__author__ = """Chris Havlin"""
__email__ = 'chris.havlin@gmail.com'
__version__ = '0.1.0'

from miscellaneouscodegen.miscellaneouscodegen import Template, TemplateCollection
from miscellaneouscodegen.unyt.dask_reductions import Reductions

template_registry = {
    "dask_reductions": [Reductions]
}
