def seosta_lapsed_ja_vanemad(fail1, fail2):
    f = open(fail1, mode="r+", encoding="UTF-8")
    g = open(fail2, mode="r+", encoding="UTF-8")
    vanemadjalapsed = {}
    dict2 = {}
    kõikkoodid = []
    kõikandmed = []
    for line in g.readlines():
        andmed = line.strip().split(" ")
        kood = andmed[0]
        nimi = andmed[1]+" "+andmed[2]
        kõikandmed.append(andmed)
        vanemadjalapsed[kood] = nimi
    for line in f.readlines():
        IDkoodid = line.strip().split(" ")
        vanemaID = IDkoodid[0]
        lapseID = IDkoodid[1]
        kõikkoodid.append(IDkoodid)
    if kood in vanemadjalapsed:
        dict2[kood] = set()
        dict2[kood].add(nimi)
    return dict2

print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
    