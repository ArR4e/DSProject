def seosta_lapsed_ja_vanemad(f1 = "lapsed.txt", f2 = "nimed.txt"):
    sõnastik = {}
    esimenefail = open(f1, "r", encoding="UTF-8")
    teinefail = open(f2, "r", encoding="UTF-8")
    nimed = []
    
    for rida in teinefail:
        isikuk, nimi = rida.strip().split(" ", 1)
        nimed.append((nimi, isikuk))
    teinefail.close()
    
    for rida in esimenefail:
        vanem, laps = rida.strip().split(" ", 1)
        for el in nimed:
            if vanem == el[1]:
                vanemnimi = el[0]
            if laps == el[1]:
                lapsnimi = el[0]
        if lapsnimi not in sõnastik:
            sõnastik[lapsnimi] = set([vanemnimi])
        else:
            n = list(sõnastik[lapsnimi])
            n.append(vanemnimi)
            n = set(n)
            sõnastik[lapsnimi] = n
    return sõnastik
            