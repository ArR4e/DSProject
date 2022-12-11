def seosta_lapsed_ja_vanemad(lapsed,nimed):
    lapsed = open(lapsed,"r")#vanema isik.k lapse isik.k
    nimed = open(nimed, "r")#isik.k nimi
    l = {}
    a = {}
    for rida in nimed:
        puhas = rida.strip()
        lahku = puhas.split()
        nimi = lahku[1] + " " + lahku[2]
        isik_k = lahku[0]
        a[isik_k] = nimi
    for rida1 in lapsed:
        puhas1 = rida1.strip()
        lahku1 = puhas1.split()
        isik_v = lahku1[0]
        isik_l= lahku1[1]
        vanem = a[isik_v]
        laps = a[isik_l]
        if laps not in l:
            l[laps] = set()
        l[laps].add(vanem)
    return l
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
