def erinevad_sümbolid(sõne):
    täht = set(sõne)
    return täht
def sümbolite_sagedus(sõne):
    sõnad = ()
    for sümbol in sõne:
        sõnad[sümbol] = sõnad.get(sümbol, 0) + 1
    return sõnad

def grupeeri(sõne):
    täishäälikud = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']
    kaashäälikud = not täishäälikud and not (' ', '-', '.')
    sõnad = ()
    vastus = ()
    thäälikud = set()
    khäälikud = set()
    muu = set()
    
    for sümbol in sõne:
        sõnad[sümbol]  = sõnad(sümbol, 0) + 1
    for i in sõnad:
        if i.lower() in täishäälikud:
            thäälikud.add(i, sõnad)
        elif i.lower() in kaashäälikud:
            khäälikud.add(i, sõnad)
        elif:
            muu.add(i, sõnad)
    
    vastus['täishäälikud'] = thäälikud
    vastus['kaashäälikud'] = khäälikud
    vastus['muu'] = muu
    return vastus

print(grupeeri('suvaline lause'))