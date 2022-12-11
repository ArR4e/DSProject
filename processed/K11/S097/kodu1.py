def seosta_lapsed_ja_vanemad(fail1, fail2):
    #sõnastik1, mis seob isikukoodi ja nime
    sõnastik1 = {}
    g = open(fail2, encoding = "UTF-8")
    for rida in g:
        ridajärjendina = list(rida.split())
        sõnastik1[ridajärjendina[0]] = " ".join(ridajärjendina[1:])
    g.close()

    #sõnastik2, mis seob lapse ja tema vanemad
    sõnastik2 = {}
    f = open(fail1, encoding = "UTF-8")
    for rida in f:
        ridajärjendina = list(rida.split())
        laps = ridajärjendina[1]
        vanem = ridajärjendina[0]
        if sõnastik1[laps] in sõnastik2:
            sõnastik2[sõnastik1[laps]].add(sõnastik1[vanem])
        else:
            vanematehulk = set()
            vanematehulk.add(sõnastik1[vanem])
            sõnastik2[sõnastik1[laps]] = vanematehulk
    f.close()
    return sõnastik2


laps_ja_tema_vanemad = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for laps in laps_ja_tema_vanemad:
    vanemad = ", ".join(laps_ja_tema_vanemad[laps])
    print(laps + ": " + vanemad)

