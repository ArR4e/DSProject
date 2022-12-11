def seosta_lapsed_ja_vanemad(lapsed, nimed):
    fail = open("lapsed.txt", encoding = "UTF-8")
    f = open("nimed.txt", encoding = "UTF-8")
    sõnastik = {}
    nimed = {}
    lapsed = set() #vanema isikukood, lapse isikukood
    for rida in fail:
        korrastatud = rida.strip().split(" ")
        lapsed.add((korrastatud[0],korrastatud[1]))  
    for rida in f:
        korrastatud = rida.strip().split(" ")
        nimed[korrastatud[0]] = korrastatud[1] + " " + korrastatud[2]        

    for isikukood, nimi in nimed.items():
        vanemad = set()
        for vanemid, lapsid in lapsed:
            if isikukood == lapsid:
                vanemad.add(nimed[vanemid])
            if len(vanemad) > 0:
                sõnastik[nimi] = vanemad
    fail.close()
    f.close()

    return sõnastik
      
    
for laps, vanemad in seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt").items():
    vanemad = list(vanemad)
    if len(vanemad) == 1:
        print(laps + ": " + vanemad[0])
    if len(vanemad) == 2:
        print(laps + ": " + vanemad[0] + ", " + vanemad[1])
