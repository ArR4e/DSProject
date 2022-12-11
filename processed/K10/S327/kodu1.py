def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sagedused = {}
    for el in sõne:
        sagedused[el] = sagedused.get(el, 0) + 1
    return sagedused
        
def grupeeri(sõne):
    täishäälikud = {}
    kaashäälikud = {}
    muud = {}
    sag = sümbolite_sagedus(sõne)
    tulemus = {}
    if sõne == "":
        tulemus['Täishäälikud'] = {}
        tulemus['Kaashäälikud'] = {}
        tulemus['Muud'] = {}
        return tulemus
    
    for täht in sag:
        if täht in "aAeEiIoOuUõÕöÖäÄüÜ":
            täishäälikud[täht] = sag[täht]
        elif täht in "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsŠšZzŽžTtVvWwXxYy":
            kaashäälikud[täht] = sag[täht]
        else:
            muud[täht] = sag[täht]

    tulemus['Täishäälikud'] = {(key, value) for key, value in täishäälikud.items()}
    tulemus['Kaashäälikud'] = {(key, value) for key, value in kaashäälikud.items()}
    tulemus['Muud'] = {(key, value) for key, value in muud.items()}
    return tulemus
    
print(grupeeri("hulk ei sisalda kunagi korduvaid elemente"))