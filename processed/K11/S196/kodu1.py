def seosta_lapsed_ja_vanemad(f2 = "lapsed.txt", f1 = "nimed.txt"):
    sõnastik = {}
    nimed = {}
    vanemad = {}
    
    with open(f1, encoding = "utf-8") as nimede_fail:
        for rida in nimede_fail:
            nimi = rida.strip().split(" ", 1)
            nimed[nimi[0]] = nimi[1]

    with open(f2, encoding = "utf-8") as vanemate_fail:
        for rida in vanemate_fail:
            vanem_laps = rida.strip().split(" ", 1)
            lapse_isikukood = vanem_laps[1]
            vanema_isikukood = vanem_laps[0]
            lapse_nimi = nimed[lapse_isikukood]
            vanema_nimi = nimed[vanema_isikukood]
            print(lapse_nimi)
            print(vanema_nimi)
            if lapse_nimi in sõnastik:
                sõnastik[lapse_nimi].add(vanema_nimi)
            else:
                sõnastik[lapse_nimi] = set([vanema_nimi])
        return sõnastik

print(seosta_lapsed_ja_vanemad())