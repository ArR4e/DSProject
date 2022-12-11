def erinevad_sümbolid(sõne):
    hulk = {i for i in sõne}
    return hulk

def sümbolite_sagedus(sõne):
    dic = {i : sõne.count(i) for i in sõne}
    return dic

def grupeeri(sõne):
    dic = {'Täishäälikud': {}, 'Kaashäälikud': {}, 'Muud': {}}
    dic['Täishäälikud'] = {(i, sõne.count(i)) for i in sõne if (i, sõne.count(i)) not in dic['Täishäälikud'] and i in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "Õ", "õ", "Ä", "ä", "Ö", "ö", "Ü", "ü"]}
    dic['Kaashäälikud'] = {(i, sõne.count(i)) for i in sõne if (i, sõne.count(i)) not in dic['Täishäälikud'] and i.isalpha()}
    dic['Muud'] = {(i, sõne.count(i)) for i in sõne if (i, sõne.count(i)) not in dic['Täishäälikud'] and (i, sõne.count(i)) not in dic['Kaashäälikud']}
    return dic