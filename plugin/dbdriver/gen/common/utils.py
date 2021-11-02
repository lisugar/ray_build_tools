import sys
from tabulate import tabulate

def CamelCase(input):
    words = input.replace('_', '-').split('-')
    name = ''
    for w in words:
        name += w.capitalize()
    return name
# end CamelCase

def Generate_data_by_order(input, order):
    ret = []
    for o in order:
        if input and o in input:
            ret.append(input.get(o))
        else:
            ret.append(None)

    return ret

def PrintObjets(headers, order, input):

    data = []

    if isinstance(input, list):
        for i in input:
            data.append(Generate_data_by_order(i, order))
    else:
        data.append(Generate_data_by_order(input, order))

    print (tabulate(data, headers=headers, tablefmt="grid"))

def PrintException(ex):
    if (sys.version_info > (3, 0)):
        print(ex)
    else:
        print(ex.message)
