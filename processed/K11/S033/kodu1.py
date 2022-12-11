def seosta_lapsed_ja_vanemad(lapsed, nimed):

    f1 = open(lapsed, encoding = "utf8")
    f2 = open(nimed, encoding = "utf8")

    #loen failist kahte järjendisse vanemate ja laste isikukoodid
    vanemad = []
    lapsed = []
    for rida in f1:
        rida = rida.strip().split()
        vanemad.append(int(rida[0]))
        lapsed.append(int(rida[1]))

    #loon sõnastiku teisest failist loetud andmetega kujul 'isikukood:nimi'
    nimed = {}
    for rida in f2:
        rida = rida.strip().split()
        nimed[int(rida[0])] = rida[1] + " " + rida[2]

    #kirjutan vanemate ja laste järjendid üle nimedega
    for i in vanemad:
        for j in nimed.keys():
            if i == j:
                vanemad[vanemad.index(i)] = nimed[j]
             
    for i in lapsed:
        for j in nimed.keys():
            if i == j:
                lapsed[lapsed.index(i)] = nimed[j]         

    #loon sõnastiku laste nimedega, millele vastavad tühjad hulgad
    sõn = {}
    for nimi in lapsed:
        if nimi not in sõn:
            sõn[nimi] = set()
    print(vanemad)
    #leian sõnastikust lapse nimele vastavad indeksid järjendis ja selle abil lisan vanema nime hulka
    for võti in sõn:
        for nimi in lapsed:
            if võti == nimi:
                indeks = lapsed.index(nimi)
                sõn[võti].add(vanemad[indeks])
                lapsed[indeks] = 'tühi'
                vanemad[indeks] = 'tühi'
    f1.close()
    f2.close()

    return sõn


print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))