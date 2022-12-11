def erinevad_sümbolid(tähtedeks):
    hulk = set()
    for i in tähtedeks:
        hulk.add(i)
    return hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for võti in erinevad_sümbolid(sõne):
        sõnastik[võti] = 0
    for täht in sõne:
        sõnastik[täht] += 1
    return sõnastik

def grupeeri(tekst):
    grupeeritud = {"Täishäälikud" : set(), "Kaashäälikud" : set(), "Muud" : set()}
    täishäälikud = "aeiouõäöü"
    kaashäälikud = "bcdfghjklmnpqrsšzžtvwxy"
    sagedus = sümbolite_sagedus(tekst)
    for võti in sagedus:
        ennik = (võti, sagedus[võti])
        if võti.lower() in täishäälikud:
            grupeeritud["Täishäälikud"].add(ennik)
        elif võti.lower() in kaashäälikud:
            grupeeritud["Kaashäälikud"].add(ennik)
        else:
            grupeeritud["Muud"].add(ennik)
    return grupeeritud