def poisse_ja_tüdrukuid(names):
    boys = 0
    girls = 0
    for el in names:
        if el[-1] == 'P':
            boys += 1
        if el[-1] == 'T':
            girls += 1
    return (boys, girls)