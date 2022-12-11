def poisse_ja_tüdrukuid(inimesed):
    poiste_arv = 0
    tudrukute_arv = 0
    for inimene in inimesed:
        if inimene[-1] == 'P':
            poiste_arv += 1
        elif inimene[-1] == 'T':
            tudrukute_arv += 1
    
    return (poiste_arv, tudrukute_arv)