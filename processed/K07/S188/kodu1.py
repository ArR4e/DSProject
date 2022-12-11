def poisse_ja_tüdrukuid(nimekiri):
    poisid = 0
    tüdrukud = 0
    for i in nimekiri:
        if i[-1] == "P":
            poisid += 1
        elif i[-1] == "T":
            tüdrukud += 1
    return (poisid, tüdrukud)