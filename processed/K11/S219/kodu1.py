def seosta_lapsed_ja_vanemad(x, y):
    f1 = open(x, "r")
    f2 = open(y, "r")

    vanemad_lapsed_sõnastik = {}
    koodid_nimed_sõnastik = {}
    sõnastik = {}
    lapsed = []
    vanemad = []

    for rida in f1:
        andmed = rida.strip().split()
        vanemad_lapsed_sõnastik[andmed[0]] = andmed[1]
        lapsed.append(andmed[1])
        vanemad.append(andmed[0])
        
    for rida in f2:
        nimed_andmed = rida.strip().split(" ", 1)
        koodid_nimed_sõnastik[nimed_andmed[0]] = nimed_andmed[1]

    vastupidi_vanemad_lapsed_sõnastik = {y:x for x,y in vanemad_lapsed_sõnastik.items()}
    vastupidi_koodid_nimed_sõnastik = {y:x for x,y in koodid_nimed_sõnastik.items()}
    laste_nimed = []
    vanemate_nimed = []
    for i in range(len(lapsed)):
        if lapsed[i] in koodid_nimed_sõnastik:
            laste_nimed.append(koodid_nimed_sõnastik[lapsed[i]])

    for nimi in laste_nimed:
        sõnastik[nimi] = set()

    abihulk = set()

    for laps in sõnastik.keys():
        lapse_kood = vastupidi_koodid_nimed_sõnastik[laps]
        if lapse_kood in lapsed:
            loendur = 0
            positsioon = []
            for i in lapsed:
                if i == lapse_kood:
                    positsioon.append(loendur)
                loendur = loendur + 1
            for indeks in positsioon:
                vanema_kood = vanemad[indeks]
                vanema_nimi = koodid_nimed_sõnastik[vanema_kood]
                abihulk.add(vanema_nimi)
                if laps in sõnastik:
                    sõnastik[laps] = abihulk
            abihulk = set()
    return(sõnastik)