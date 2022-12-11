def erinevad_sümbolid(sone):
    return set(sone)

def sümbolite_sagedus(sone):
    sumbolid = erinevad_sümbolid(sone)
    sonastik = {}
    for el in sumbolid:
        sonastik[el] = sone.count(el)
    return sonastik

def grupeeri(sone):
    sonastik = {"Täishäälikud" : set(),
                "Kaashäälikud" : set(),
                "Muud" : set()
                }
    taishaalikud = "aeiouõäöüAEIOUÕÖÄÖÜ"
    kaashaalikud = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
    sumbolid = erinevad_sümbolid(sone)
    for el in sumbolid:
        if el in taishaalikud:
            sonastik["Täishäälikud"].add((el, sone.count(el)))
        elif el in kaashaalikud:
            sonastik["Kaashäälikud"].add((el, sone.count(el)))
        else:
            sonastik["Muud"].add((el, sone.count(el)))
    return sonastik