def poisse_ja_tüdrukuid(nimed):
    poisse = 0
    tüdrukuid = 0
    for i in nimed:
        if i.endswith(' T'):
            tüdrukuid += 1
        elif i.endswith(' P'):
            poisse += 1
    return (poisse, tüdrukuid)


            
            
        
        