def poisse_ja_tüdrukuid(nimekiri):
    poisse=0
    tüdrukuid=0
    for nimi in nimekiri:
        if nimi[-1]=='P':
            poisse+=1
        elif nimi[-1]=='T':
            tüdrukuid+=1
    return (poisse,tüdrukuid)