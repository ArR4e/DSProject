def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return(hulk)

def sümbolite_sagedus(sõne):
    kõik = []
    sõnastik = {}
    for täht in sõne:
        kõik += [täht]
    for element in kõik:
        if element in sõnastik:
            sõnastik[element] = sõnastik[element] + 1
        else:
            sõnastik[element] = 1
    return(sõnastik)
        
def grupeeri(sõne):
    täishäälikud = {"a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"}
    kaashäälikud = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "z", "x", "y"}
    grupp = {}
    grupp["täishäälikud"] = set()
    grupp["kaashäälikud"] = set()
    grupp["muud"] = set()
    for element in sümbolite_sagedus(sõne):
        if element.lower() in täishäälikud:
            grupp["täishäälikud"].add((element))
            grupp["täishäälikud"].add((sümbolite_sagedus(sõne)[element]))
        elif element.lower() in kaashäälikud:
            grupp["kaashäälikud"].add((element))
            grupp["kaashäälikud"].add((sümbolite_sagedus(sõne)[element]))
        else:
            grupp["muud"].add((element))
            grupp["muud"].add((sümbolite_sagedus(sõne)[element]))
    print(grupp)
    
grupeeri("tere tere vanakere")