def seosta_lapsed_ja_vanemad(f1, f2):
    f1 = open("lapsed.txt", "r", encoding = "UTF-8")
    f2 = open("nimed.txt", "r", encoding = "UTF-8")
    
    
    sõnastik = {}
    pere = {}
    for rida in f1:
        a = rida.strip().split(" ")
        sõnastik[a[1]] = a[0]

    sõnastik2 = {}
    for rida in f2:
        b = rida.strip().split(" ", 1)
        isikukood = b[0]
        nimi = b[1]
        sõnastik2[isikukood] = nimi
     

    
    for võti in sõnastik2:
        if võti in sõnastik:
            lapse_nimi = sõnastik2[võti]
            vanema_nimi = sõnastik2[sõnastik[võti]]
            if isikukood == võti:
                if lapse_nimi not in pere:
                    pere[lapse_nimi] = set()
                    vanem = sõnastik2[sõnastik[võti]]
                    pere[lapse_nimi].add(vanem)
                    continue
                    
            else:
                vanema_laps = sõnastik2[võti]
                if vanema_laps not in pere:
                    pere[vanema_laps] = set()
                    pere[vanema_laps].add(vanema_nimi)
                else:
                    pere[vanema_laps].add(vanema_nimi)
                    continue

    
    f1.close()
    f2.close()

    return pere
        

    
print(seosta_lapsed_ja_vanemad("lapsed.py", "nimed.py"))        


            