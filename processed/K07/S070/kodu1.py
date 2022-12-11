def poisse_ja_tüdrukuid(sõnede_kogum):
    poisse = 0
    tüdrukuid = 0
    for lapsi in sõnede_kogum:
        tagur_pidi = lapsi [::-1]
        esi_täht = tagur_pidi [:1]
        if esi_täht == "P":
            poisse += 1
        if esi_täht == "T":
            tüdrukuid += 1
    return (poisse, tüdrukuid)
        
            
        