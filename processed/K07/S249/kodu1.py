def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    
    for i in järjend:
        järg = i.split(" ")
        sugu = järg[-1]
        
        
        if sugu == "P":
            poisse += 1
        if sugu == "T":
            tüdrukuid += 1
        
        
        
    return (poisse, tüdrukuid)
