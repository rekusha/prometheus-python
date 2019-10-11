import sys

x, y = int(sys.argv[1]), int(sys.argv[2])

def clean_list(x):
    output_list = []
    for i in x:
        if i not in output_list:
            output_list.append(i)
    return output_list

def counter(x, y):
    x, y = str(x), str(y)
    con = 0
    for i in clean_list(x):
        if i in clean_list(y):
            con += 1
    print int(con)