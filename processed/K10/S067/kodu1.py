def erinevad_sümbolid(x):
    if x == '':
        return set()
    return set(x)
def sümbolite_sagedus(x):
    sagedus = {}
    a = list(erinevad_sümbolid(x))
    for i in a:
        sagedus[i] = x.count(i)
    return sagedus
def grupeeri(x):
    sõnastik = {}
    täishäälikud = ['a', 'e', 'o', 'i', 'u', 'ö', 'ä', 'ü', 'õ']
    kaashäälikud = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y']
    y = sümbolite_sagedus(x)
    täis = []
    kaas = []
    muud = []
    for i in y:
        if i.lower() in täishäälikud:
            täis.append((i, y[i]))
        elif i.lower() in kaashäälikud:
            kaas.append((i, y[i]))
        else:
            muud.append((i, y[i]))
            
    sõnastik['Täishäälikud'] = set(täis)
    sõnastik['Kaashäälikud'] = set(kaas)
    sõnastik['Muud'] = set(muud)
    return sõnastik
print(grupeeri('sõida tasa üle silla'))