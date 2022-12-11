def poisse_ja_tüdrukuid(järjend):
    tüdrukud = 0
    poisid = 0
    for el in järjend:
        if el[-1] == "T":
            tüdrukud += 1
        elif el[-1] == "P":
            poisid += 1
    poisid_ja_tüdrukud = (poisid,tüdrukud)
    return poisid_ja_tüdrukud