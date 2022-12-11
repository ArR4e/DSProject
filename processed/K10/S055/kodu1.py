def erinevad_sümbolid(a):
    return set([t2ht for t2ht in a])

def sümbolite_sagedus(a):
    dicts = {}
    erinevad = erinevad_sümbolid(a)
    for t2ht in erinevad:
        dicts[t2ht] = a.count(t2ht)
    return dicts

def grupeeri(a):
    t2is = "aeiouõäöü"
    kaas = "bdghjklmnprstvxqyzwfc"
    sagedused = sümbolite_sagedus(a)
    
    _t2is = []
    _kaas = []
    _muud = []
    
    for el in sagedused.items():
        if el[0] in t2is or el[0] in t2is.upper():
            _t2is.append(el)
        elif el[0] in kaas or el[0] in kaas.upper():
            _kaas.append(el)
        else:
            _muud.append(el)

    return {'Täishäälikud': set(_t2is), 'Kaashäälikud': set(_kaas), 'Muud': set(_muud)}
