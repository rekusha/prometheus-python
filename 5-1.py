import sys

def clean_list(x):
    output_list = []
    for i in x:
        typ = type(i)
        if i not in output_list:
            output_list.append(i)
        if i in output_list:
            if type(i) != type(output_list[output_list.index(i)]):
                output_list.append(typ(i))
    return output_list

print clean_list(list(sys.argv[1:]))
