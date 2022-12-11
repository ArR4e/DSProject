def seosta_lapsed_ja_vanemad(fail1, fail2):
    f1 = open(fail1, encoding="utf-8")
    lapsed_sisu = f1.readlines()
    f1.close()

    f2 = open(fail2, encoding="utf-8")
    nimed_sisu = f2.readlines()
    f2.close()
    
    lapsed = [rida.strip().split(" ") for rida in lapsed_sisu]
    nimed = [rida.strip().split(" ", 1) for rida in nimed_sisu]
    
    tulemus = {}
    
    for n in nimed:
        laps = ""
        vanemad = []
        for l in lapsed:
            if n[0] == l[1]:
                laps = n[1]
                for _n in nimed:
                    if _n[0] == l[0]:
                        vanemad.append(_n[1])
        if laps and vanemad:
            tulemus[laps] = set(vanemad)

    return tulemus
    

print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
