
def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    d = {}
    for arv in sõne:
        d[arv] = d.get(arv, 0) + 1
    return d

def grupeeri(sõne):
    
    täishäälikud = {"a","e","i","o","u","õ","ä","ö","ü"}
    kaashäälikud = {"q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","ž","š","x","c","v","b","n","m"}
    muu = set(sõne) - (täishäälikud|kaashäälikud)
    #tsõne = täishäälikud & set(sõne)
    #ksõne = kaashäälikud & set(sõne)
    #msõne = muu & set(sõne)
    sümbolite_sagedus(sõne)
    tn = set()
    kn = set()
    mn = set()
    for ib in sõne:
        bn = (ib, sümbolite_sagedus(sõne)[ib])
        if ib in täishäälikud:
           tn.add(bn)
        elif ib in kaashäälikud:
            kn.add(bn)
        elif ib in muu:
            mn.add(bn)
        
            
    an = {'Täishäälikud': tn, 'Kaashäälikud': kn, 'Muud': mn}
    return an
    