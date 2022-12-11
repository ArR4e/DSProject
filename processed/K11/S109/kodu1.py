def seosta_lapsed_ja_vanemad(lapsed, nimed):
    sõnastik1 = {}
    sõnastik2 = {}
    fail2 = open(nimed)
    for rida in fail2:
        r = rida.strip("\n").split(" ", 1)
        if len(r) >= 2:
            isikukood = r[0]
            nimi = " ".join(r[1:])
            sõnastik2[isikukood] = nimi
            
        if isikukood in sõnastik2:
            True
        else:
            print("no")
    return sõnastik2
        
    fail1 = open(lapsed)
    for rida in fail1:
        r = rida.strip("\n").split(" ")


    