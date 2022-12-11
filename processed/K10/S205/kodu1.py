def erinevad_sümbolid(sõne):
    hulk = set()
    for täht in sõne:
        hulk.add(täht)
    return hulk

def sümbolite_sagedus(sõne):
    d={}
    for täht in sõne:
        d[täht] = d.get(täht, 0) +1
    return d

def grupeeri(sõne):
    d={}
    täishäälikud = 'aeiouõäöüAEIOUÕÄÖÜ'
    kaashäälikud = 'bcdfghjklmnpqrstvwxyzšžBCDFGHJKLMNPQRSTVWXYZŠŽ'
    täishäälikud_sõnastik = {}
    kaashäälikud_sõnastik = {}
    muud_sõnastik = {}
    for täht in sõne:
        if täht in täishäälikud:
            täishäälikud_sõnastik[täht] = täishäälikud_sõnastik.get(täht, 0) +1
        elif täht in kaashäälikud:
            kaashäälikud_sõnastik[täht] = kaashäälikud_sõnastik.get(täht, 0) +1
        else:
            muud_sõnastik[täht] = muud_sõnastik.get(täht, 0) +1
    d['Täishäälikud'] = set(list(täishäälikud_sõnastik.items()))
    d['Kaashäälikud'] = set(list(kaashäälikud_sõnastik.items()))
    d['Muud'] = set(list(muud_sõnastik.items()))
    return d
    