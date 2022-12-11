def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for rida in järjend:
        uus_järjend = rida.split(" ")
        a = uus_järjend[-1]
        if a == "P":
            poisse += 1
        else:
            tüdrukuid += 1
    return (poisse, tüdrukuid)
        
        
        
