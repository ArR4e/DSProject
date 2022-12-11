def erinevad_sümbolid(sõne):
    hulk = set()
    for el in sõne:
        hulk.add(el)
    return hulk
        
def sümbolite_sagedus(sõne):
    sõnastik = {}
    for el in sõne:
        if el not in sõnastik:
            sõnastik[el] = sõne.count(el)
    return sõnastik

def grupeeri(sõne):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    for el in sõne:
        if el.lower() in "aeiouõäöü":
            sõnastik["Täishäälikud"].add((el,sõne.count(el)))
        elif el.lower() in "bdfghjklmnprsšzžtvxyqwc":
            sõnastik["Kaashäälikud"].add((el,sõne.count(el)))
        else:
            sõnastik["Muud"].add((el,sõne.count(el)))
    return sõnastik