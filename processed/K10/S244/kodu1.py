def erinevad_sümbolid(lause):
    hulk = set()
    for el in lause:
        hulk.add(el)
    return hulk
    
def sümbolite_sagedus(lause):
    sõnastik = {}
    for täht in lause:
        if täht in sõnastik:
            sõnastik[täht] = sõnastik[täht] + 1
        else:
            sõnastik[täht] = 1
    return sõnastik

def grupeeri(lause):
    x = {}
    täishäälikud = ('a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü')
    kaashäälikud = ('b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm','c', 'n', 'p', 'r', 's','z', 't', 'v','š', 'ž', 'y', 'w', 'q', 'x')
    x['Täishäälikud'] = set()
    x['Kaashäälikud'] = set()
    x['Muud'] = set()
    y = sümbolite_sagedus(lause)
    for täht in lause:
        if täht.lower() in täishäälikud:
            lisa = (täht, y[täht])
            x["Täishäälikud"].add(lisa)
        elif täht.lower() in kaashäälikud:
            lisa = (täht, y[täht])
            x["Kaashäälikud"].add(lisa)
        else:
            lisa = (täht, y[täht])
            x["Muud"].add(lisa)
    return x


   
lause = input('Sisestage lause: ')
print(erinevad_sümbolid(lause))
print(sümbolite_sagedus(lause))
print(grupeeri(lause))