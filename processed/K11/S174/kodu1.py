def seosta_lapsed_ja_vanemad(fnimi_lapsed, fnimi_nimed):
    sõnastik = {}
    fnimi_lapsed = "lapsed.txt"
    fnimi_nimed = "nimed.txt"
    isikukoodid = open(fnimi_lapsed, "r", encoding = "UTF-8")
    isikukood_nimi = open(fnimi_nimed, "r", encoding = "UTF-8")
    nimed = []
    for rida in isikukood_nimi:
        kood, nimi = rida.strip().split(" ", 1)
        nimed.append((nimi, kood))
    isikukood_nimi.close()
    for rida in isikukoodid:
        vanem, laps = rida.strip().split(" ", 1)
        for el in nimed:
            if vanem == el[1]:
                nimi_vanem = el[0]
            if laps == el[1]:
                nimi_laps = el[0]
        if nimi_laps not in sõnastik:
            sõnastik[nimi_laps] = set([nimi_vanem])
        else:
            sõnastik2 = list(sõnastik[nimi_laps])
            sõnastik2.append(nimi_vanem)
            sõnastik2 = set(sõnastik2)
            sõnastik[nimi_laps] = sõnastik2
    return sõnastik
        
#print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
    