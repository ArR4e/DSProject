
def erinevad_sümbolid (sõne):
    hulk = set()
    for täht in sõne:
        hulk.add(täht)
    return hulk

def sümbolite_sagedus(sõne):
    d = {}
    for täht in sõne:
        d[täht] = d.get(täht, 0) + 1
    return d

def grupeeri (sõne):
    täishäälikud = 'AEIOUÕÄÖÜaeiouõäöü'
    kaashäälikud = 'BCDFGHJKLMNPQRSŠZŽTVWXUZbcdfghjklmnpqrsšzžtvwxyz'
    t = {}
    k = {}
    m = {}
    for el in sõne:
        if el in täishäälikud:
            t[el] = t.get(el, 0) + 1
        elif el in kaashäälikud:
            k[el] = k.get(el, 0) + 1
        else:
            m[el] = m.get(el, 0) + 1
    th = set()
    kh = set()
    mh = set()
    for el in t.keys():
        th.add((el, t[el]))
    for el in k.keys():
        kh.add((el, k[el]))
    for el in m.keys():
        mh.add((el, m[el]))
        
    return {'Täishäälikud':th, 'Kaashäälikud':kh, 'Muud':mh}