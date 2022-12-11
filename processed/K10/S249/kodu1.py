def erinevad_sümbolid(sõne):
    tähed = set(sõne)
    return tähed

def sümbolite_sagedus(sõne):
    d = {}
    for täht in sõne:
        if täht in d:
            d[täht] = d[täht] + 1
        else:
            d[täht] = 1
    return d

def grupeeri(sõne):
    täishäälikud = "aeiouõäöüAEIOUÕÄÖÜ"
    kaashäälikud = "bcdfghjklmnpqrsšzžtvwxyBCDFGHJKLMNPQRSŠZŽTVWXY"
    vokaal = {}
    kaas = {}
    muu = {}
    for märk in sõne:
        
        if märk in täishäälikud:
            if märk in vokaal:
                vokaal[märk] = vokaal[märk] + 1
            else:
                vokaal[märk] = 1
                
        elif märk in kaashäälikud:
            if märk in kaas:
                kaas[märk] = kaas[märk] + 1
            else:
                kaas[märk] = 1
                
        else:
            if märk in muu:
                muu[märk] = muu[märk] + 1
            else:
                muu[märk] = 1
    v = set(vokaal.items())
    k = set(kaas.items())
    m = set(muu.items())
    return {"Täishäälikud" : v, "Kaashäälikud" : k, "Muud" : m}  
