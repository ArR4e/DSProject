#poiste ja tüdrukute arv

def poisse_ja_tüdrukuid(järjend):
    tüdrukuid=0
    poisse=0
    for el in järjend:
        sugu=el[-1]
        if sugu == "T":
            tüdrukuid+=1
        if sugu == "P":
            poisse+=1
    return (poisse, tüdrukuid)
            