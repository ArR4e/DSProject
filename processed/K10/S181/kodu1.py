def erinevad_sümbolid(lause):
    return set(lause)

def sümbolite_sagedus(lause):
    sõnastik1 = {}
    for x in lause:
        sõnastik1[x] = sõnastik1.get(x, 0)+1
    return sõnastik1

def grupeeri(lause):
    sagedus = sümbolite_sagedus(lause)
    täishäälikud = (*list("aeiouõäöü"),)
    kaashäälikud = (*list("bcdfghjklmnpqrsšzžtvwxy"),)
    sõnastik = {"Täishäälikud": set(), "Kaashäälikud": set(),"Muud": set()}
    for el in sagedus:
        if el.lower() in täishäälikud:
            sõnastik["Täishäälikud"].add((el, sagedus[el]))
        elif el.lower() in kaashäälikud:
            sõnastik["Kaashäälikud"].add((el,sagedus[el]))
        else:
            sõnastik["Muud"].add((el, sagedus[el]))
    return sõnastik
    
print(grupeeri("sõida tasa üle silla"))