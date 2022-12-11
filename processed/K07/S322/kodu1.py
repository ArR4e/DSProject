def poisse_ja_tüdrukuid(inimesed):
    # poisside arv
    p = 0
    # tüdrukute arv
    t = 0
    for inimene in inimesed:
        # tükelda, vt kas viimane tükk on P või T
        if inimene.split()[-1] == "P":
            p += 1
        elif inimene.split()[-1] == "T":
            t += 1
    # tagasta ennak
    return (p, t)
