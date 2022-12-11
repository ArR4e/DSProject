def erinevad_sümbolid(sone):
    return set(sone)

def sümbolite_sagedus(sone):
    sonastik = {}
    for symbol in erinevad_sümbolid(sone):
        sonastik[symbol] = sone.count(symbol)
    return sonastik

def grupeeri(sone):
    sonastik = sümbolite_sagedus(sone)
    tais = set()
    kaas = set()
    muud = set()
    for voti in sonastik:
        if voti in "aeuioäöüõAEUIOÄÖÜÕ":
            tais.add((voti,sonastik[voti]))
        elif voti in "qwrtypsdfghjklzxcvbnmšžQWRTYPSDFGHJKLZXCVBNMŠŽ":
            kaas.add((voti,sonastik[voti]))
        else:
            muud.add((voti,sonastik[voti]))
    grupid = {"Täishäälikud": tais, "Kaashäälikud": kaas, "Muud": muud}
    return grupid
