

def poisse_ja_tüdrukuid(lapsed):
    tüdrukute_arv = 0
    poiste_arv = 0
    for laps in lapsed:     
        viimane_täht = laps[-1]
        if viimane_täht == 'T':
            tüdrukute_arv += 1
        else:
            poiste_arv += 1
         
    kokku = (poiste_arv, tüdrukute_arv)
    return(kokku)
    
