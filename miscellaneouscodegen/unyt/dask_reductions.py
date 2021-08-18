import sys


# reductions that maintain units
reductions = [
        "mean", 
        "max",
        "min",
        "sum",
        "median",
        "std",
        "cumsum",
        "var",
        ]

reductions += [f"nan{i}" for i in reductions]


fun_template = [
        "def func_name(unyt_da, *args, **kwargs)\n",
        "    result = dask.array.func_name(unyt_da, *args,**kwargs)\n",
        "    return _create_with_quantity(result, unyt_da._unyt_array)\n\n\n"
        ]


func_template_pairs = [ (redu, fun_template) for redu in reductions ]


def write_reductions(filename: str):

    # reductions that need a unit check
    with open(filename,'w') as fi:
        fi.write("# dask.array.reductions\n\n\n")

    for redu, template in func_template_pairs:
        for ln in template:
            fi.write(ln.replace("func_name", redu))

if __name__ == '__main__':
    if len(sys.varg) < 2:
        raise ValueError("provide a filename")
    filename = sys.varg[1]
    write_reductions(filename)
    print(f"wrote reductions to {filename}")
