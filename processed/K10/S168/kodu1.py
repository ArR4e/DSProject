def erinevad_sümbolid(str):
    sümbolite_hulk = set()
    for i in str:
        sümbolite_hulk.add(i)
    return(sümbolite_hulk)

def sümbolite_sagedus(str):
    d = {}
    for i in str:
        d[i] = d.get(i, 0) + 1
    return(d)

def grupeeri(str):
    täishäälikud = ('e', 'u', 'i', 'o', 'ü', 'õ', 'a', 'ö', 'ä')
    kaashäälikud = ('q', 'y', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm')
    d = {'Täishäälikud': {}, 'Kaashäälikud': {}, 'Muud': {}}
    hulk_1 = set()
    hulk_2 = set()
    hulk_3 = set()
    for i in str:
        if i.lower() in täishäälikud:
            hulk_1.add((i, str.count(i)))
        elif i.lower() in kaashäälikud:
            hulk_2.add((i, str.count(i)))
        else:
            hulk_3.add((i, str.count(i)))
    d['Täishäälikud'] = hulk_1
    d['Kaashäälikud'] = hulk_2
    d['Muud'] = hulk_3
    return(d)
    
        