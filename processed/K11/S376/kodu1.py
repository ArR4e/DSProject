def seosta_lapsed_ja_vanemad(lapsed, nimed):
    lapsed = open(lapsed, "r", encoding="UTF-8")
    nimed = open(nimed, "r", encoding="UTF-8")

    s = {}
    tulemus = {}

    vanemate_koodid = set()
    laste_koodid = set()
    ik_paarid = []
    laps_ja_vanem_paarid = []

    for rida in nimed:
        rida = rida.strip().split(" ", 1)
        isikukood = int(rida[0])
        nimi = rida[1]
        s[isikukood] = nimi
        
    for rida in lapsed:
        rida = rida.strip().split()
        vanema_ik = int(rida[0])
        lapse_ik = int(rida[1])
        vanemate_koodid.add(vanema_ik)
        laste_koodid.add(lapse_ik)
        ik_paarid += [[vanema_ik, lapse_ik]]

    for kood, nimi in s.items():
        if kood in laste_koodid and s[kood] not in tulemus:
            tulemus[s[kood]] = set()
        
        if kood in vanemate_koodid:
            for paar in ik_paarid:
                if kood in paar and kood != paar[1]:
                    laps_ja_vanem_paarid += [[s[paar[1]], s[kood]]]

    for võti, väärtus in laps_ja_vanem_paarid:
        tulemus.setdefault(võti).add(väärtus)
    
    lapsed.close()
    nimed.close()
    return tulemus

for laps, vanemad in seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt").items():
    print(laps + ": " + ", ".join(vanemad))