import string

def poisse_ja_tüdrukuid(NimiSugu):
    poisse=0
    tüdrukuid=0
    x = ((str(NimiSugu)).replace("',","").replace("']","").split()) 
    for el in x:
        if el == "P":
            poisse= poisse + 1
            continue
        elif el== "T":
            tüdrukuid= tüdrukuid +1
            continue
        else:
            continue
        
    return poisse, tüdrukuid

