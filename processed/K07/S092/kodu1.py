def poisse_ja_tüdrukuid(arg):
    boys = 0
    girls = 0
    for el in arg:
        if el[-1] == "P":
            boys += 1
        elif el[-1] == "T":
            girls += 1
    return (boys, girls)