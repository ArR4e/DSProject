def erinevad_sümbolid(sõne):
    sümbolite_hulk = set()
    for el in sõne:
        sümbolite_hulk.add(el)
    return(sümbolite_hulk)

def sümbolite_sagedus(sõne):
    sümbolite_esinemissagedus = dict()
    for el in sõne:
        sümbolite_esinemissagedus[el] = sümbolite_esinemissagedus.get(el, 0) + 1
    return(sümbolite_esinemissagedus)

def grupeeri(sõne):
    täishäälikud = ('a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü')
    kaashäälikud = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y', 'z')
    sõnastik = dict()
    sõnastik['Täishäälikud'] = set()
    sõnastik['Kaashäälikud'] = set()
    sõnastik['Muud'] = set()
    sümbolite_esinemissagedus = sümbolite_sagedus(sõne)
    for võti in sümbolite_esinemissagedus:
        if võti.lower() in täishäälikud:
            esinemissagedus = sümbolite_esinemissagedus[võti]
            sõnastik['Täishäälikud'].add((võti, esinemissagedus))
        elif võti.lower() in kaashäälikud:
            esinemissagedus = sümbolite_esinemissagedus[võti]
            sõnastik['Kaashäälikud'].add((võti, esinemissagedus))
        else:
            esinemissagedus = sümbolite_esinemissagedus[võti]
            sõnastik['Muud'].add((võti, esinemissagedus))
    return(sõnastik)
#print(erinevad_sümbolid('Programmeerimine on arvutiprogrammide lähtekoodi kirjutamise, testimise, silumise ja haldamise tegevuste jada'))
#print(sümbolite_sagedus('Hei hopsti, väikevend!'))
#print(grupeeri('Hei hopsti, väikevend!'))