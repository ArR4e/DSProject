def seosta_lapsed_ja_vanemad(lapsed, nimed):
    l = open(lapsed, encoding="UTF-8")
    n = open(nimed, encoding="UTF-8")
    d = {}
    lapsed = set()
    nimistik = {}
    for rida in l:
        a = rida.strip().split(" ")
        lapsed.add((a[0],a[1]))
    for rida in n:
        a = rida.strip().split(" ")
        nimistik[a[0]] = a[1] + " " + a[2]
    l.close()
    n.close()
    for isikukood, nimi in nimistik.items():
        vanemad = set()
        for v_id, l_id in lapsed:
            if isikukood == l_id:
                vanemad.add(nimistik[v_id])
        if len(vanemad) > 0:
            d[nimi] = vanemad
    return d

   
for laps, vanemad in seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt").items():
    vanemad = list(vanemad)
    if len(vanemad) == 1:
        print(laps + ": " + vanemad[0])
    elif len(vanemad) == 2:
        print(laps + ": " + vanemad[0] + ", " + vanemad[1])
            
