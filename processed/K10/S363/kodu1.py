def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    
    return hulk

def sümbolite_sagedus(sõne):
    d = {}
    for i in sõne:
        if i not in d.keys():
            d[i] = sõne.count(i)
            
    return d

def grupeeri(sõne):
    täishäälikud = "AEIOUÕAÖÜaeiouõäöü"
    kaashäälikud = "BCDFGHJKLMNPQRSŠZŽTVWXYbcdfghjklmnpqrsšzžtvwxy"
    d = {}
    ühine = set(täishäälikud) & set(sõne)
    täishäälikuid = set()
    for i in ühine:
        täishäälikuid.add((i, sõne.count(i)))
        
    d['Täishäälikud'] = täishäälikuid
    
    ühine = set(kaashäälikud) & set(sõne)
    kaashäälikuid = set()
    for i in ühine:
        kaashäälikuid.add((i, sõne.count(i)))
    
    d['Kaashäälikud'] = kaashäälikuid
    
    üle = set(sõne) - (set(kaashäälikud)|set(täishäälikud))
    muud = set()
    for i in üle:
        muud.add((i, sõne.count(i)))
        
    d['Muud'] = muud
    
    return d

        
        
        
        