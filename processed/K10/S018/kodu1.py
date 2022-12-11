def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for sümb in sõne:
        sõnastik[sümb] = sõnastik.get(sümb, 0) + 1
    return sõnastik

def grupeeri(sõne):
    täishäälikud = "iüueöõoäaIÜUEÖÕOÄA"
    kaashäälikud = "cxywqbdfghjklmnprsšzžtvCXYWQBDFGHJKLMNPRSZTVŽŠ"
    kõik_sümb = erinevad_sümbolid(sõne)
    sagedus = sümbolite_sagedus(sõne)
    täish = set()
    kaash = set()
    sümbolid = set()
    väl_sõnastik = {}
    for sümb in kõik_sümb:
        if sümb in täishäälikud:
            täish.add((sümb, sagedus[sümb]))
        elif sümb in kaashäälikud:
            kaash.add((sümb, sagedus[sümb]))
        else:
            sümbolid.add((sümb, sagedus[sümb]))
    väl_sõnastik["Täishäälikud"] = täish
    väl_sõnastik["Kaashäälikud"] = kaash
    väl_sõnastik["Muud"] = sümbolid
    return väl_sõnastik