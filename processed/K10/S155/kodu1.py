def erinevad_sümbolid(sõne):
    if sõne == '':
        return set()
    else:
        for el in sõne:
            hulk = set(sõne)
        return hulk

def sümbolite_sagedus(sõne):
    sagedus = {}
    jrj = list(sõne)
    for el in jrj:
        if el in sagedus:
            sagedus[el] += 1
        else:
            sagedus[el] = 1
    return sagedus

def grupeeri(sõne):
    täishäälik = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü', 'A', 'E', 'I', 'O',
    'U', 'Õ', 'Ä', 'Ö', 'Ü']
    kaashäälik = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                  'p', 'r', 's', 'š', 'ž', 't', 'v', 'c', 'q', 'z', 'w', 'y', 'x',
                  'B', 'D', 'F', 'G' ,'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'Š',
                  'Z', 'Ž', 'T', 'V', 'C', 'Q', 'W', 'Y', 'X']
    
    d = {'Täishäälikud': {}, 'Kaashäälikud': {}, 'Muud': {}}
    
    sagedus = {}
    jrj = list(sõne)
    for el in jrj:
        if el in sagedus:
            sagedus[el] += 1
        else:
            sagedus[el] = 1
    a = set()
    b = set()
    ab = set()
    for el in sagedus.items():
        if el[0] in täishäälik:
            a.add(el)
            continue
        if el[0] in kaashäälik:
            b.add(el)
            continue
        else:
            ab.add(el)
            continue
        
    d['Täishäälikud'] = a
    d['Kaashäälikud'] = b
    d['Muud'] = ab
    
    return d 
    
sõne = 'rumalused, rumalused ja veelkord rumalused'
print(grupeeri(sõne))
        


