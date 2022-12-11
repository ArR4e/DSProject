def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sõnastik_sagedus = {}
    for i in sõne:
        if i in sõnastik_sagedus:
            sõnastik_sagedus[i] += 1
        else:
            sõnastik_sagedus[i] = 1
    return sõnastik_sagedus

def grupeeri(sõne):
    sõnastik_grupp = {}
    sõnastik_grupp['Täishäälikud'] = set()
    sõnastik_grupp['Kaashäälikud'] = set()
    sõnastik_grupp['Muud'] = set()
    for x in sõne:
        if x.lower() in 'aeiouõäöü':
            sõnastik_grupp['Täishäälikud'].add((x, sümbolite_sagedus(sõne).get(x)))
        elif x.lower() in 'bcdfghjklmnpqrstvwxyz':
            sõnastik_grupp['Kaashäälikud'].add((x, sümbolite_sagedus(sõne).get(x)))
        else:
            sõnastik_grupp['Muud'].add((x, sümbolite_sagedus(sõne).get(x)))
    return sõnastik_grupp