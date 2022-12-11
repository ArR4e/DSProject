def poisse_ja_tüdrukuid(l):
    p = 0
    t = 0
    for i in l:
        if i[-1] == "P":
            p += 1
        else:
            t += 1
    return p, t