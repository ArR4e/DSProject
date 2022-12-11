def erinevad_sümbolid(sõne):
    vastus = set(sõne)
    return vastus

def sümbolite_sagedus(sõnastikuks):
    sõnastik = {}
    for taht in sõnastikuks:
        sõnastik[taht] = sõnastik.get(taht, 0) + 1
    return sõnastik

def grupeeri(loendatav):
    taishaalikud = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']
    kaashaalikud = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y']
    taish = set()
    kaash = set()
    muud = set()
    sonastik = {"Täishäälikud": taish, "Kaashäälikud": kaash, "Muud": muud}
    sagedus = sümbolite_sagedus(loendatav)
    for voti in sagedus.keys():
        ennik = (voti, sagedus[voti])
        if voti.lower() in taishaalikud:
            taish.add(ennik)
        elif voti.lower() in kaashaalikud:
            kaash.add(ennik)
        else:
            muud.add(ennik)
    return sonastik