def seosta_lapsed_ja_vanemad(lapsed,nimed):
    lapsed = open("lapsed.txt", encoding="utf-8")
    nimed = open("nimed.txt", encoding="utf-8")
    sõnastik = {}
    sõnastik2 = {}
    for rida in nimed:
        eraldi = rida.split()
        nimi_osadena = eraldi[1:]
        nimi = " ".join(nimi_osadena)
        sõnastik2[eraldi[0]] = nimi
    for el in lapsed:
        i = el.split()
        nimi = sõnastik2[i[1]]
        nimi_vanem = sõnastik2[i[0]]
        if nimi in sõnastik:
            sõnastik[nimi].add(nimi_vanem)
        if nimi not in sõnastik:
            sõnastik[nimi] = set()
            sõnastik[nimi].add(nimi_vanem)
    lapsed.close()
    nimed.close()
    return sõnastik

print(seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt"))