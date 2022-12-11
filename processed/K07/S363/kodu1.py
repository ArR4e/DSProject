def poisse_ja_tüdrukuid(nimed):
    poisse = 0
    tüdrukuid = 0
    
    for i in nimed:
        ühik = i.split()
        pikkus = len(ühik)
        sugu = ühik[pikkus-1]
        
        if sugu == "P":
            poisse += 1
            
        if sugu == "T":
            tüdrukuid += 1
            
    return (poisse, tüdrukuid)
