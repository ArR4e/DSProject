def erinevad_sümbolid(sõne):
    h = set(sõne)
    return(h)

def sümbolite_sagedus(sõne):
    s1 = {}
    for el in sõne:
        s1[el] = s1.get(el,0) +1
    return(s1)

def grupeeri(sõne):
    s2 = {}
    sagedus = sümbolite_sagedus(sõne)
    s2['Täishäälikud'] =set()
    s2['Kaashäälikud'] =set()
    s2['Muud'] =set()
    for võti, väärtus in sagedus.items():
        if võti.lower() in 'aeiouõäöü':
            s2['Täishäälikud'].add((võti,väärtus))
        elif võti.lower() in 'bcdfghjklmnpqrsšzžtvxyw':
            s2['Kaashäälikud'].add((võti,väärtus))
        else:
            s2['Muud'].add((võti,väärtus))
    return s2


print(grupeeri("sõida tasa üle silla"))