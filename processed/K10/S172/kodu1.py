def erinevad_sümbolid(tekst):
    tulemus = set()
    for elem in tekst:
        tulemus.add(elem)
        
    return tulemus

def sümbolite_sagedus(tekst):
    symbols = erinevad_sümbolid(tekst)
    tulemus = {}
    for symb in symbols:
        tulemus[symb]=tekst.count(symb)
        
    return tulemus

def grupeeri(tekst):
    symbols = erinevad_sümbolid(tekst)
    sagedused = sümbolite_sagedus(tekst)
    vokaalid = {'a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü'}
    kaas = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
            'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y'}
    täishäälikud = set()
    kaashäälikud = set()
    muud = set()
    
    for elem in symbols:
        if elem.lower() in vokaalid:
            täishäälikud.add((elem, sagedused[elem]))
        elif elem.lower() in kaas:
            kaashäälikud.add((elem, sagedused[elem]))
        else:
            muud.add((elem, sagedused[elem]))
            
    tulemus = {'Täishäälikud': täishäälikud, 'Kaashäälikud': kaashäälikud,
               'Muud': muud}
    return tulemus