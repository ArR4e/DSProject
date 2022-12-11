def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    
    for nimi in järjend:
        sugu = nimi[-1]
        if sugu == "P":
            poisse +=1
        else:
            tüdrukuid +=1
    return(poisse, tüdrukuid)