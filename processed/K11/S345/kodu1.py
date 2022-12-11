def seosta_lapsed_ja_vanemad(laste_fail, nimede_fail):
    f = open(laste_fail)
    järjend = []
    järjend2 = []
    sõnastik = {}
    for rida in f:
        vanemad = set()
        järjend = rida.strip().split()
        lapse_id = järjend[1]
        vanema_id = järjend[0]
        f2 = open(nimede_fail)
        for r in f2:
            järjend2 = r.strip().split()
            if lapse_id == järjend2[0]:
                lapse_nimi = str(järjend2[1] + " " + järjend2[2])
            elif vanema_id == järjend2[0]:
                vanema_nimi = str(järjend2[1] + " " + järjend2[2])
                vanemad.add(vanema_nimi)
        if lapse_nimi in sõnastik:
            sõnastik[lapse_nimi].add(vanema_nimi)
        else:
            sõnastik[lapse_nimi] = vanemad
        f2.close()
    f.close()
    return sõnastik

pere = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for võti in pere:
    vanemad = ""
    n = 0
    for el in pere[võti]:
        vanemad += str(el)
        if n == 0:
            vanemad += ", "
        n += 1
    print(võti + ": " + vanemad)