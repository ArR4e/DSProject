def seosta_lapsed_ja_vanemad(fail1, fail2):
    fail1 = open("lapsed.txt", encoding = "UTF-8")
    fail2 = open("nimed.txt", encoding = "UTF-8")
    sõnastik = {}
    
    lisasõnastik = {}
    for rida in fail2:
        rida = rida.strip().split(" ", 1)
        isikukood = rida[0]
        nimi = rida[1]
        lisasõnastik[isikukood] = nimi

    for isikukoodid in fail1:
        lapse_nimi = ""
        isikukoodid = isikukoodid.split()
        vanema_isikukood = isikukoodid[0]
        lapse_isikukood = isikukoodid[1]
        if lapse_isikukood in lisasõnastik:
            lapse_nimi = lisasõnastik[lapse_isikukood]
            if lisasõnastik[lapse_isikukood] not in sõnastik:
                sõnastik[lapse_nimi] = set()
        if lisasõnastik[vanema_isikukood] not in sõnastik[lapse_nimi]:
            sõnastik[lapse_nimi].add(lisasõnastik[vanema_isikukood])
            
    fail1.close()
    fail2.close()
    
    return sõnastik

print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))