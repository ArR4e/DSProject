def poisse_ja_tüdrukuid(järjend):
    poisse = tüdrukuid = 0
    for inimene in järjend:
        inimene = inimene.split(" ")
        sugu = inimene[-1]
        if sugu == "P":
            poisse +=1
        elif sugu == "T":
            tüdrukuid +=1
    return(poisse,tüdrukuid)