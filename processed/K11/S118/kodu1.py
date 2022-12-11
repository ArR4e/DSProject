def seosta_lapsed_ja_vanemad(lapsed_failinimi, nimed_failinimi):
    lapsed_fail = open(lapsed_failinimi, "r", encoding="utf-8")
    nimed_fail = open(nimed_failinimi, "r", encoding="utf-8")
    
    vanemad_lapsed_koodid = {}
    nimed_ja_koodid = {}
    viimased_seosed = {}
    lapsed_vanemad = {}
    
    for rida in lapsed_fail.readlines():
        if rida.strip().split()[1] not in vanemad_lapsed_koodid:
            vanemad_lapsed_koodid[rida.strip().split()[1]] = set()
            vanemad_lapsed_koodid[rida.strip().split()[1]].add(rida.strip().split()[0])
        else:
            vanemad_lapsed_koodid[rida.strip().split()[1]].add(rida.strip().split()[0])
    
    for rida in nimed_fail.readlines():
        terve_nimi = ""
        terve_nimi+=rida.strip().split()[1]
        for nimi in rida.strip().split()[2:]:
            terve_nimi+=" "+nimi
        nimed_ja_koodid[rida.strip().split()[0]] = terve_nimi
    
    for lapse_kood in vanemad_lapsed_koodid:
        lapse_nimi = ""
        for kood in nimed_ja_koodid:
            if lapse_kood == kood:
                lapse_nimi = nimed_ja_koodid[kood]
        vanemate_koodide_hulk = vanemad_lapsed_koodid[lapse_kood]
        vanemate_nimed = set()
        for vanema_kood in vanemate_koodide_hulk:
            for kood in nimed_ja_koodid:
                if kood == vanema_kood:
                    vanemate_nimed.add(nimed_ja_koodid[kood])
        lapsed_vanemad[lapse_nimi] = vanemate_nimed
    lapsed_fail.close()
    nimed_fail.close()
    return lapsed_vanemad
    
sõnastik = seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")

for laps in sõnastik:
    vanemad = ""
    vanemate_arv = 1
    for vanem in sõnastik[laps]:
        if vanemate_arv > 1:
            vanemad+=", "+vanem
        else:
            vanemad+=vanem
            vanemate_arv+=1
    print(laps + ":",vanemad)