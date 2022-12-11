def poisse_ja_tüdrukuid(jrj):
    p = 0
    t = 0
    for rida in jrj:
        if rida[-1] == "P":
            p += 1
        else:
            t += 1
    return (p, t)