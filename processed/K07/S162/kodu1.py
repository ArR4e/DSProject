def poisse_ja_tüdrukuid(järjend):
    tüdrukuid=0
    poisse=0
    for nimi in järjend:
        if nimi.split()[-1]=='T':
            tüdrukuid+=1
        if nimi.split()[-1]=='P':
            poisse+=1
    return(poisse, tüdrukuid)
