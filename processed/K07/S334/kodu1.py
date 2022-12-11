def poisse_ja_tüdrukuid(n):
    boys = 0
    girls = 0
    for person in n:
        if person[-1] == 'P':
            boys += 1
        elif person[-1] == 'T':
            girls += 1
    return boys, girls if boys > 0 or girls > 0 else 0
