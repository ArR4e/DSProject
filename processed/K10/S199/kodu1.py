def erinevad_sümbolid(sõne):
    tähed = set()
    for el in sõne:
        if el not in tähed:
            tähed.add(el)
    return(tähed)

def sümbolite_sagedus(sõne):
    sagedus = {}
    for el in (erinevad_sümbolid(sõne)):
        kordus = sõne.count(el)
        sagedus[el] = kordus
    return(sagedus)
    
def grupeeri(sõne):
    täis = {}
    täis[0] = "Täishäälikud"
    kaas = {}
    kaas[0] = "Kaashäälikud"
    muu = {}
    muu[0] = "Muud"
    for täht in sümbolite_sagedus(sõne):
        if 
    