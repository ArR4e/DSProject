def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for el in järjend:
        if el[-1] == "P":
            m += 1
        if el[-1] == "T":
            n += 1
    return(m, n)