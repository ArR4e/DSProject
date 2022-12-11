def seosta_lapsed_ja_vanemad(f_lapsed, f_nimed):
    lapsed = open(f_lapsed, encoding="UTF-8")
    nimed = open(f_nimed, encoding="UTF-8").readlines()
    isikukoodid = {}
    for rida in nimed:
        andmed = rida.strip().split()
        isikukoodid[andmed[0]] = andmed[1] + " " + andmed[2]
    seosta = {}
    for rida in lapsed:
        andmed = rida.strip().split()
        if isikukoodid[andmed[1]] in seosta:
            seosta[isikukoodid[andmed[1]]].add(isikukoodid[andmed[0]])
        else:
            seosta[isikukoodid[andmed[1]]] = set([isikukoodid[andmed[0]]])
    return seosta

seostatud = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

for indeks in seostatud:
    print(indeks + ": " + ", ".join(seostatud[indeks]))
        