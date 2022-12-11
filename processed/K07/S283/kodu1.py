def poisse_ja_tüdrukuid(järjend):
    tüdrukuid = 0
    poisse = 0
    for i in järjend:
        if " T" in i:
            tüdrukuid += 1
        if " P" in i:
            poisse += 1
    return(poisse, tüdrukuid)
        
järjend = []
print(poisse_ja_tüdrukuid(järjend))