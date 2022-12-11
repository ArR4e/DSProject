def erinevad_sümbolid(s):
    return set(s)

def sümbolite_sagedus(s):
    jär = list(s)
    d = {}
    for a in jär:
        d[a] = d.get(a, 0) + 1
    return d

def grupeeri(s):
    täis = list('aeiouõäöüAEIOUÕÄÖÜ')
    kaas = list('bcdfghjklmnpqrsšzžtvwxyBCDFGHJKLMNPQRSŠZŽTVWXY')
    sõnejär = list(s)
    d = {}
    d['Täishäälikud'] = set()
    d['Kaashäälikud'] = set()
    d['Muud'] = set()
    b = sümbolite_sagedus(s)
    for a in b:
        if a in täis:
            d['Täishäälikud'].add((a, b[a]))
        elif a in kaas:
            d['Kaashäälikud'].add((a, b[a]))
        else:
            d['Muud'].add((a, b[a]))
    return d

print(grupeeri("sõida tasa üle silla"))