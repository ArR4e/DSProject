def erinevad_sümbolid(sõne):
    hulk = set()
    for täht in sõne:
        hulk.add(täht)
    return hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for täht in sõne:
        palju = sõne.count(täht)
        sõnastik[täht] = palju
    return sõnastik

def grupeeri(sõne):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    sagedus = sümbolite_sagedus(sõne)
    for sümbol in sagedus:
        if sümbol in "aeiouõäöü":
            sõnastik["Täishäälikud"].add((sümbol,sagedus[sümbol]))
        elif sümbol in "qwrtypsdfghjklzxcvbnm":
            sõnastik["Kaashäälikud"].add((sümbol,sagedus[sümbol]))
        else:
            sõnastik["Muud"].add((sümbol,sagedus[sümbol]))
    return sõnastik
