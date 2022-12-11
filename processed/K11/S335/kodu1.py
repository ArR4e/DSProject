def seosta_lapsed_ja_vanemad(fail1, fail2):
    
    f1 = open(fail1)
    v_isik = []
    l_isik = []
    for rida in f1:
        j = rida.strip().split(" ")
        v_isik.append(j[0])
        l_isik.append(j[1])
    f1.close()
    
    f2 = open(fail2, encoding = "UTF-8")
    sõn = {}
    for rida1 in f2:
        j2 = rida1.strip().split(" ")
        sõn[j2[1]+ " " + j2[2]] = j2[0]
    f2.close()
    
    lapsed = {}
    vanemad = {}
    i = 0
    for nimi, kood in sõn.items():
        if kood in l_isik:
            lapsed[nimi] = kood
        if kood in v_isik:
            vanemad[kood] = nimi
        i += 1
        if i > len(l_isik):
            break

    f3 = open(fail1)
    sõn2 = {}
    for rida3 in f3:
        j2 = rida3.strip().split(" ")
        for nimi1, kood1 in lapsed.items():
            a = []
            if j2[1] == kood1:
                a.append(vanemad[j2[0]])
                if nimi1 in sõn2:
                    a.append(sõn2[nimi1][0])
                    sõn2[nimi1] = a
                    sõn2[nimi1] = a
                else:
                    sõn2[nimi1] = a
                    sõn2[nimi1] = a
    for nimi2, hulk in sõn2.items():
        uus = set(hulk)
        sõn2[nimi2] = uus
    return sõn2
                
                
for laps, vanemad1 in seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt").items():
    jär = list(vanemad1)
    if len(jär) == 1:
        print(laps + ": " + jär[0])
    else:
        print(laps + ": " + jär[0] + ", " + jär[1])