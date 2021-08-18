from miscellaneouscodegen import Template, TemplateCollection

class Reduction(Template):
    def empty_template(self):

        fun_template = [
                "def func_name(unyt_da, *args, **kwargs)\n",
                "    result = dask.array.func_name(unyt_da, *args,**kwargs)\n",
                "    return _create_with_quantity(result, unyt_da._unyt_array)\n\n\n"
        ]

        return fun_template, ['func_name']


class Reductions(TemplateCollection):

    def __init__(self):

        # reductions that maintain units
        redus = [
                  "mean",
                  "max",
                  "min",
                  "sum",
                  "median",
                  "std",
                  "cumsum",
                  "var",
                  ]

        redus += [f"nan{i}" for i in redus]
        list_of_templates = [Reduction(replace_dict={'func_name': r}) for r in redus]
        super().__init__(list_of_templates)


