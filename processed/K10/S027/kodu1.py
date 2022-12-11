def erinevad_sümbolid(sõne):
    hulk = set()
    for el in sõne:
        hulk.add(el)
    return hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for täht in sõne:
        sõnastik[täht] = sõne.count(täht)
    return sõnastik

def grupeeri(sõne):
    grupid = {}
    grupid['Täishäälikud'] = set()
    grupid['Kaashäälikud'] = set()
    grupid['Muud'] = set()
    sõnastik = sümbolite_sagedus(sõne)
    for el in sõnastik:
        ennik = (el, sõnastik[el])
        if el in 'aAeEiIoOuUõÕäÄöÖüÜ':
            grupid['Täishäälikud'].add(ennik)
        elif el in 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsSšŠzZžŽtTvVwWxXyY':
            grupid['Kaashäälikud'].add(ennik)
        else:
            grupid['Muud'].add(ennik)
    return grupid

print(grupeeri("sõida tasa üle silla"))
            