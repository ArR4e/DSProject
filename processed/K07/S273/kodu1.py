def poisse_ja_tüdrukuid(järjend):
    p = 0
    t = 0
    for nimi in järjend:
        if nimi[-1] == "P":
            p += 1
        if nimi[-1] == "T":
            t += 1
    return (p, t)