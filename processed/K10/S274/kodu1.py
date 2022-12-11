def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk

def sümbolite_sagedus(sõne):
    d = {}
    for el in sõne:
        d[el] = d.get(el, 0) + 1
    return d

def grupeeri(sõne):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    d_sagedus = sümbolite_sagedus(sõne)
    for el in d_sagedus:
        ennik = (el, d_sagedus[el])
        täishäälik = "aeiouõäöü"
        kaashäälik = "bdfghjklmnprsšzžtv"
        if el.lower() in täishäälik:
            sõnastik["Täishäälikud"].add(ennik)
        elif el.lower() in kaashäälik:
            sõnastik["Kaashäälikud"].add(ennik)
        else:
            sõnastik["Muud"].add(ennik)
    return sõnastik