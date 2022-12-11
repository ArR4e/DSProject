#Teksti analüüs
def erinevad_sümbolid(sõne):
    sümbolite_hulk = set()
    for element in sõne:
        sümbolite_hulk.add(element)
    return sümbolite_hulk

def sümbolite_sagedus(sõne):
    sagedused = {}
    for element in sõne:
        if element in sagedused:
            sagedused[element] += 1
        else:
            sagedused[element] = 1
    return sagedused

def grupeeri(sõne):
    grupeeritud = {"Täishäälikud": {}, "Kaashäälikud": {}, "Muud": {}}
    sümbolite_hulk = erinevad_sümbolid(sõne)
    täish_hulk = set()
    kaash_hulk = set()
    muud_hulk = set()
    for element in sümbolite_hulk:
        if element.lower() in "aeiouõäöü":
           täish_hulk.add((element, sümbolite_sagedus(sõne)[element]))
        elif element.lower() in "bcdfghjklmnprqsšzžtvwxy":
           kaash_hulk.add((element, sümbolite_sagedus(sõne)[element]))
        else:
            muud_hulk.add((element, sümbolite_sagedus(sõne)[element]))
    grupeeritud["Täishäälikud"] = täish_hulk
    grupeeritud["Kaashäälikud"] = kaash_hulk
    grupeeritud["Muud"] = muud_hulk
    return grupeeritud