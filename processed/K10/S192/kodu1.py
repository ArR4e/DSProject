def erinevad_sümbolid(sõne):
    erinev_sümbol = set()
    for sümbol in sõne:
        if sümbol not in erinev_sümbol:
            erinev_sümbol.add(sümbol)
        else:
            continue
    return erinev_sümbol

def sümbolite_sagedus(sõne):
    erinevad_sümbolid_sagedus = {}
    for sümbol in sõne:
        if sümbol not in erinevad_sümbolid_sagedus:
            erinevad_sümbolid_sagedus[sümbol] = 1
        else:
            erinevad_sümbolid_sagedus[sümbol] = erinevad_sümbolid_sagedus[sümbol] + 1
    return erinevad_sümbolid_sagedus

def grupeeri(sõne):
    täishäälikud = 'aeiouõäöü'
    grupeeritud_sümbolid = sümbolite_sagedus(sõne)
    grupeeritud_sümbolid_sagedus = {}
    grupeeritud_sümbolid_sagedus['Täishäälikud'] = set()
    grupeeritud_sümbolid_sagedus['Kaashäälikud'] = set()
    grupeeritud_sümbolid_sagedus['Muud'] = set()
    for sümbol in grupeeritud_sümbolid:
        if sümbol.lower() in täishäälikud and sümbol.isalpha():
            grupeeritud_sümbolid_sagedus['Täishäälikud'].add((sümbol, grupeeritud_sümbolid[sümbol]))
        elif sümbol.lower().isalpha() == True:
            grupeeritud_sümbolid_sagedus['Kaashäälikud'].add((sümbol, grupeeritud_sümbolid[sümbol]))
        else:
            grupeeritud_sümbolid_sagedus['Muud'].add((sümbol, grupeeritud_sümbolid[sümbol]))
    return grupeeritud_sümbolid_sagedus
grupeeri("sõida tasa üle silla")

#erinevad_sümbolid_sõnastik = erinevad_sümbolid(sõne)
#erinev_sümbol_sagedus = {}
#for erinev_sümbol in erinevad_sümbolid_sõnastik:
#        sümbol_sagedus = 0
#        for sümbol in sõne:
#            if sümbol in erinev_sümbol:
#                sümbol_sagedus += 1
#        erinev_sümbol_sagedus[erinev_sümbol] = sümbol_sagedus
#return(erinev_sümbol_sagedus)