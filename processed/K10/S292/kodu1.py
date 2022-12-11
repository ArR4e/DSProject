def erinevad_sümbolid(sõne):
    hulk = set()
    for täht in sõne:
        hulk.add(täht)
    return hulk

#print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))


def sümbolite_sagedus(sõne):
    tähed = {}
    for täht in sõne:
        if täht in tähed:
            tähed[täht] = tähed[täht] + 1
        else:
            tähed[täht] = 1
    return tähed
        
#print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(sõne):
    
    grupp = {}
    t2is = ""
    kaas = ""
    muu = ""
    
    for täht in sõne:
        if täht in {"a","e","i","o","u","õ","ä","ö","ü","A","E","I","O","U","Õ","Ä","Ö","Ü"}:
            t2is = t2is+täht
        elif täht in {"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","š","z","ž","t","v","w","x","y",
                            "B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","Š","Z","Ž","T","V","W","X","Y"}:
            kaas = kaas+täht
        else:
            muu = muu+täht

    t2is = sümbolite_sagedus(t2is)
    hulk = set()
    for symbol in t2is:
        hulk.add((symbol, t2is[symbol]))
    grupp['Täishäälikud'] = hulk

    kaas = sümbolite_sagedus(kaas)
    hulk = set()
    for symbol in kaas:
        hulk.add((symbol, kaas[symbol]))
    grupp['Kaashäälikud'] = hulk

    muu = sümbolite_sagedus(muu)
    hulk = set()
    for symbol in muu:
        hulk.add((symbol, muu[symbol]))
    grupp['Muud'] = hulk
    
    return grupp