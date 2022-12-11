def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for i in järjend:
        if i[-1] == "T":
            tüdrukud += 1
        if i[-1] == "P":
            poisid += 1
    return (poisid, tüdrukud)

