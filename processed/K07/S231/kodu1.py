# Poiste ja tüdrukute arv
def poisse_ja_tüdrukuid(x):
    p = 0
    t = 0
    for nimi in x:
        if nimi[-1] == "P":
            p += 1
        elif nimi[-1] == "T":
            t += 1
    return (p, t)
