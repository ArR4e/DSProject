def seosta_lapsed_ja_vanemad(väiksed, info):
    ühend=open(väiksed)
    nimed=open(info)
    kelle_laps={}
    inimesed={}
    for rida in nimed:
        rida = rida.strip()
        andmed=rida.split(" ")
        inimesed[andmed[0]]=andmed[1]+ " " +andmed[2]
    for rida in ühend:
        rida = rida.strip()
        andmed=rida.split(" ")
        if inimesed[andmed[1]] not in kelle_laps.keys():
            kelle_laps[inimesed[andmed[1]]]={inimesed[andmed[0]]}
        elif inimesed[andmed[1]] in kelle_laps.keys():
            kelle_laps[inimesed[andmed[1]]].add(inimesed[andmed[0]])
    #vanemad_ja_lapsed={}
    #print(andmed)
    #print(inimesed)
    #print('inimesed', inimesed)
    #print('kelle', kelle_laps)
    
    '''for isik in kelle_laps.keys():
        print(isik)
        if inimesed[isik] not in vanemad_ja_lapsed.keys():
            e=[]
            for e in kelle_laps[isik]:
                e+=inimesed[kelle_laps[isik]]
            print(vanemad_ja_lapsed)
            vanemad_ja_lapsed[inimesed[isik]]=set(e)'''
    
        

    
    return kelle_laps
    
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))