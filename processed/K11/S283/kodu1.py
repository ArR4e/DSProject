def seosta_lapsed_ja_vanemad(f_laps, f_nimi):
    f_lapsed = open(f_laps, encoding="utf-8")
    f_nimed = open(f_nimi, encoding="utf-8")
    sõnastik = {}
    lisa = {}
    for rida in f_nimed:
        inimesed = rida.strip().split(" ",1)
        lisa[inimesed[0]] = inimesed[1]
    for rida in f_lapsed:
        ik_list = rida.strip().split() #vanem[0], laps[1]
        if lisa[ik_list[1]] not in sõnastik:
            sõnastik[lisa[ik_list[1]]] = set()
        sõnastik[lisa[ik_list[1]]].add(lisa[ik_list[0]])
    f_lapsed.close()
    f_nimed.close()
    return sõnastik
        

