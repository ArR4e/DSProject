def poisse_ja_tüdrukuid(nimed):
    poisse=0
    tüdrukuid=0
    
    for nimi in nimed:
        osad = nimi.split()
        if osad[-1]=="P":
            poisse=poisse + 1
        elif osad[-1]=="T":
            tüdrukuid=tüdrukuid + 1
    return (poisse, tüdrukuid)
print (poisse_ja_tüdrukuid([]))