def poisse_ja_tüdrukuid(people):
    boys = 0
    girls = 0

    for i in people:
        if i.split(" ")[-1] == "P":
            boys += 1
        if i.split(" ")[-1] == "T":
            girls += 1

    return (boys, girls)