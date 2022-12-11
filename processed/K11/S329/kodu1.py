# 1. Lapsed ja vanemad

def seosta_lapsed_ja_vanemad(fail1, fail2):
    f = open(fail1, "r", encoding = "UTF-8")
    sõnastik = {}
    for rida1 in f:
        rida1 = rida1.strip().split()
        vanema_isikukood = rida1[0]
        lapse_isikukood = rida1[1]
        g = open(fail2, "r", encoding = "UTF-8")
        for rida2 in g:
            rida2 = rida2.strip().split()
            kood = rida2[0]
            nimi = ' '.join(rida2[1:])
            if vanema_isikukood == kood:
                b = nimi
            if lapse_isikukood == kood:
                a = nimi
        sõnastik.setdefault(a, []).append(b)
        g.close()
    for el in sõnastik:
        väärtus = set(sõnastik[el])
        sõnastik[el] = väärtus
    f.close()
    return sõnastik

fail1 = "lapsed.txt"
fail2 = "nimed.txt"
sõnastik = seosta_lapsed_ja_vanemad(fail1, fail2)

#print(sõnastik)
for el in sõnastik:
    print(el + ": " + ', '.join(sõnastik[el]))

