def poisse_ja_tüdrukuid(j2rjend):
    poisse = 0
    tydrukuid = 0
    for i0 in j2rjend:
        if i0.endswith("P"):
            poisse += 1
        elif i0.endswith("T"):
            tydrukuid += 1
        
        '''nimi_ja_sugu = i0.rsplit(" ")
        sugu = nimi_ja_sugu[-1]
        if sugu == "P":
            poisse += 1
        elif sugu == "T":
            tydrukuid += 1'''
    return (poisse, tydrukuid)


poisse_ja_tüdrukuid([])