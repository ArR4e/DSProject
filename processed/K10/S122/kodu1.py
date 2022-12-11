def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    tähed = {}
    for täht in sõne:
        if täht in tähed:
            tähed[täht]+=1
        else:
            tähed[täht] = 1
    return tähed

def grupeeri(sõne):
    kaashäälikud = {"c","y","b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p","q", "r", "s", "z", "t", "v","w","x"}
    täishäälikud = {"a","e","i","o","u","õ","ä","ö","ü"}
    kaas =set()
    täis = set()
    muu= set()
    grupeeritud = {}
    a = sümbolite_sagedus(sõne)
    for täht in sõne:
        võti=a.get(täht)
        el = (täht,võti)
        täht=täht.lower()
        if täht in kaashäälikud:
            kaas.add(el)
        elif täht in täishäälikud:
            täis.add(el)
        else:
            muu.add(el)
        
    grupeeritud["Kaashäälikud"]=kaas
    grupeeritud["Täishäälikud"]=täis
    grupeeritud["Muud"]=muu
    
    return(grupeeritud)
        
