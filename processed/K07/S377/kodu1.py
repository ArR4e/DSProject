#poistejatüdrukutearv
#mirjampirn
def poisse_ja_tüdrukuid(sone):
    poisse=0
    tydrukuid=0
    for el in sone:
        sugu=el[(len(el)-1):]
        if sugu=="T" or sugu=="t":
            tydrukuid+=1
        elif sugu=="P" or sugu=="p":
            poisse+=1
        else:
            print("Sugu pole õige!")
    return (poisse,tydrukuid)