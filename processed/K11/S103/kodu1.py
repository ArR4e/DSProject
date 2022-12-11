def seosta_lapsed_ja_vanemad(lapsed, nimed):
    f_lapsed = open(lapsed, encoding="utf-8")
    f_nimed = open(nimed, encoding="utf-8")
    nimed = {}
    lapsed = set()
    d = {}
    for rida in f_lapsed:
        andmed = rida.strip().split(" ")
        lapsed.add((andmed[0],andmed[1]))
    for rida in f_nimed:
        andmed = rida.strip().split(" ")
        nimed[andmed[0]] = andmed[1] + " " + andmed[2]
    f_lapsed.close()
    f_nimed.close()
    
    for isikukood, nimi in nimed.items():
        vanemad = set()
        for vanema_isikukood, lapse_isikukood in lapsed:
            if isikukood == lapse_isikukood:
                vanemad.add(nimed[vanema_isikukood])
        if len(vanemad) > 0:
            d[nimi] = vanemad
    return d
    
for laps, vanemad in seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt").items():
    vanemad = list(vanemad)
    if len(vanemad) == 1:
        print(laps + ": " + vanemad[0])
    elif len(vanemad) == 2:
        print(laps + ": " + vanemad[0] + ", " + vanemad[1])


