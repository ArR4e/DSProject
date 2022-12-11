def poisse_ja_tüdrukuid(a):
    p = 0
    t = 0
    for i in a:
        c = i[-1:].upper()
        if c == "P":
            p += 1
        elif c == "T":
            t += 1
    e = (p, t)
    return e