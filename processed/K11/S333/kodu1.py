def seosta_lapsed_ja_vanemad(lapsed_fail, nimed_fail):
    f_lapsed= open(lapsed_fail,'r',encoding='UTF-8')
    f_nimed= open(nimed_fail,'r',encoding='UTF-8')

    lapsed= {}

    #võtame laste faili ja teeme sõnastiku, kus lapsele vastavad vanemad
    for rida in f_lapsed:
        rida=rida.strip('\n').split()
        laps=rida[1]
        vanem=rida[0]
        #otsime sõnastikust lastele vanemat, kui pole, tekitame sinna tühja järjendi
        vanemad= lapsed.get(laps,[])
        vanemad.append(vanem)
        lapsed[laps]=vanemad
    #seostame isikukoodid ja nimed

    nimed={}
    for rida in f_nimed:
        rida=rida.strip('\n').split()
        isikukood= rida[0]
        #nimed võiks olla ühe elemendi all
        nimi= ' '.join(rida[1:])
        nimed[isikukood]= nimi

    f_lapsed.close()
    f_nimed.close()

    lapsed_vanemad={}
    #paneme laste ja vanemate nimed kokku
    for laps,vanemad in lapsed.items():
        lapsenimi=nimed[laps]
        #vanemaid võib mitu olla, seega koostame hulga
        vanematenimed=set()
        for nimi in vanemad:
            vanematenimed.add(nimed[nimi])
        lapsed_vanemad[lapsenimi]=vanematenimed
    
    return lapsed_vanemad
    
tulemus= seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

for laps, vanem in tulemus.items():
    print(laps,': ',', '.join(list(vanem)))
    #vanemate hulga muudame listiks ja siis ühendame komaga