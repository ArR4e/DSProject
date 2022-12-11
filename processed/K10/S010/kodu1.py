def erinevad_sümbolid(sõne):
    return set(list(sõne))

def sümbolite_sagedus(sõne):
    d={}
    for sümbol in list(sõne):
        if sümbol in d:
            d[sümbol]=d[sümbol]+1
        else:
            d[sümbol]=1
    return d

def grupeeri(sõne):
    d={}
    t=set()
    k=set()
    m=set()
    d['Täishäälikud']=t
    d['Kaashäälikud']=k
    d['Muud']=m
    sõnastik=sümbolite_sagedus(sõne)
    for võti in sõnastik:
        if võti.lower() in 'aeiouõäöü':
            t.add((võti,sõnastik[võti]))
        elif võti.lower() in 'bcdfghjklmnpqrsšzžtvwxy':
            k.add((võti,sõnastik[võti]))
        else:
            m.add((võti,sõnastik[võti]))
    return d
