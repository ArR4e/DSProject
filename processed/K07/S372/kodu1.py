def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for el in järjend:
        if el[-1] == "P":
            poisid += 1
        else:
            tüdrukud += 1
    return(poisid, tüdrukud)