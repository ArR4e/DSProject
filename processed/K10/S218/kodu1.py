def erinevad_sümbolid(sõne):
    sümbolid = set()
    for elem in sõne:
        sümbolid.add(elem)
    return sümbolid

def sümbolite_sagedus(sõne):
    sagedus = {}
    for täht in sõne:
        if täht in sagedus:
            sagedus[täht] +=1
        else:
            sagedus[täht] = 1
    return sagedus

def grupeeri(sõne):
    sümbolid = ["Täishäälikud", "Kaashäälikud", "Muud"]
    täishäälikud = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü", "A", "E", "I", "O", "U", "Õ", "Ö", "Ü", "Ä"]
    kaashäälikud = ["c", "C", "q","Q", "y", "Y", "x", "X", "ž", "Ž", "z", "Z", "d", "g", "b", "t", "r","m", "n", "p", "l", "k", "j", "h", "t", "p", "h", "s", "v", "n","D","G", "B","T","R","M","N","P","L","K","J","H","S","V","N","w","W","f","F"]
    muud = [",", " ",";", ":", "-", "_","?","!", "'", '"', "'","."] 
    grupeeritud = {}
    grupeeritud["Täishäälikud"] = set()
    grupeeritud["Kaashäälikud"] = set()
    grupeeritud["Muud"] = set()
    täis = {}
    kaas = {}
    sümbolid={}
    
    
    for täht in sõne:
        if täht in täishäälikud:
            if täht in täis:
                täis[täht] +=1
            else:
                täis[täht] = 1
        
        elif täht in kaashäälikud:
            if täht in kaas:
                kaas[täht] +=1
            else:
                kaas[täht] = 1
        elif täht in muud:
            if täht in sümbolid:
                sümbolid[täht] +=1
            else:
                sümbolid[täht] = 1
                
    for elem in täis:
        
        grupeeritud["Täishäälikud"].add((elem,täis[elem] ))
    for elem in kaas:
        grupeeritud["Kaashäälikud"].add((elem,kaas[elem]))
    for elem in sümbolid:
        grupeeritud["Muud"].add((elem, sümbolid[elem]))        
                
            
    return grupeeritud
        
    
    
    
#print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))
#print(sümbolite_sagedus("Hei hopsti, väikevend!"))
#print(grupeeri("sõida tasa üle silla"))