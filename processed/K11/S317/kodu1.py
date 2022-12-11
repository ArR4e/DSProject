def seosta_lapsed_ja_vanemad(a, b):
    f1 = open(a, "r", encoding="UTF-8")
    f2 = open(b, "r", encoding="UTF-8")
    kõikõigesti = {}
    lapsed = {}
    suur = {}
    vanemad = {}
    maatriks = []
    for i in f2:
        rida = i.strip().split(" ", 1)
        kõikõigesti[rida[0]] = rida[1]
    for i in f1:
        rida = i.strip().split()
        if rida[1] not in lapsed:
            lapsed[rida[1]] = kõikõigesti[rida[1]]
        if rida[0] in lapsed:
            lapsed[rida[1]] = lapsed[rida[1]]
        maatriks.append(rida)
    for i in lapsed:
        if lapsed[i] not in suur:
            suur[lapsed[i]] = set()
        if lapsed[i] in suur:
            suur[lapsed[i]] = suur[lapsed[i]]
    for paar in maatriks:
        suur[suur[lapsed[paar[1]]].add(kõikõigesti[paar[0]])] = suur[lapsed[paar[1]]].add(kõikõigesti[paar[0]])
    suur.pop(None)
    return suur
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")