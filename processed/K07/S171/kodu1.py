def poisse_ja_tüdrukuid(a):
    poisse = 0
    tüdrukuid = 0
    for i in a:
        if i[len(i)-1] == "P":
            poisse += 1
        else:
            tüdrukuid += 1
    return (poisse, tüdrukuid)


            