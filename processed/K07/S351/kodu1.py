def poisse_ja_tüdrukuid(järjend):
    poisse=0
    tüdrukuid=0
    for el in järjend:
        if el[-1]=="P":
            poisse+=1
        else:
            tüdrukuid+=1
    ennik=(poisse, tüdrukuid)
    return ennik

