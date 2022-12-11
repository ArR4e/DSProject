def poisse_ja_tüdrukuid(järjend):
    t = 0
    p = 0
    for rida in järjend:
        uus_järjend = rida[-1]
        if uus_järjend == "T":
            t += 1
        if uus_järjend == "P":
            p += 1
    return (p, t)

