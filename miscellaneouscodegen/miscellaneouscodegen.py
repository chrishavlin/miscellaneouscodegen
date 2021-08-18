"""Main module."""


class TemplateCollection:
    def __init__(self, list_of_templates):
        self.list_of_templates = list_of_templates

    def write(self, filename, header=None):
        with open(filename, 'w') as fi:
            if header:
                fi.write(header+"\n\n\n")

            for ntemp, t in enumerate(self.list_of_templates):
                if len(t.filled_template) == 0:
                    print(f"warning: template {ntemp} is not filled")

                for ln in t.filled_template:
                    fi.write(ln)


def fill_line(ln, replace_dict):
    for key, val in replace_dict.items():
        ln = ln.replace(key, val)
    return ln


class Template:

    def __init__(self, replace_dict=None):
        self.line_list, self.replaceable_strings = self.empty_template()
        self.filled_template = []
        if replace_dict:
            self.fill_template(replace_dict)

    def _validate_replace_dict(self, replace_dict: dict):
        for k, v in replace_dict.items():
            if k not in self.replaceable_strings:
                raise ValueError(f"{k} is not a valid template string, please check replaceable_strings")
            if type(v) is not str:
                raise ValueError(f"{k} value must be a string")

    def fill_template(self, replace_dict: dict):
        self._validate_replace_dict(replace_dict)
        for ln in self.line_list:
            f_ln = fill_line(ln, replace_dict)
            self.filled_template.append(f_ln)

    def empty_template(self):
        # needs to returna the template as a list of strings and a list of strings
        # that are allowed to be replaced
        raise NotImplementedError

