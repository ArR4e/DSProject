def erinevad_sümbolid(sõne):
    if len(sõne) > 0:
        hulk = {sõne[0]}
        for element in sõne[1:]:
            if element not in hulk:
                hulk.add(element)
        return hulk
    else:
        return set()

#print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(sõne):
    sümbolite_sagedus = {}
    for element in sõne:
        if element not in sümbolite_sagedus:
            sümbolite_sagedus[element] = 1
        else:
            sümbolite_sagedus[element]+=1
    return sümbolite_sagedus

#print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(sõne):
    täishäälikud = ["I","Ü","U","E","Ö","Õ","O","Ä","A","i","ü","u","e","ö","õ","o","ä","a"]
    kaashäälikud = ["Y","y","W","w","X","x","C","c","Q","q","B", "D", "F", "G", "H", "J", "K", "L"
                    , "M", "N", "P", "R", "S", "S", "Z", "Z"
                    , "T", "V","b", "d", "f", "g", "h", "j"
                    , "k", "l", "m", "n", "p", "r"
                    , "s", "s", "z", "z", "t", "v"]
    täishäälikuid = set()
    kaashäälikuid = set()
    muid = set()
    sagedus = sümbolite_sagedus(sõne)
    for element in sagedus:
        if element in täishäälikud:
            täishäälikuid.add((element, sagedus[element]))
        elif element in kaashäälikud:
            kaashäälikuid.add((element, sagedus[element]))
        else:
            muid.add((element, sagedus[element]))
    return {"Täishäälikud": täishäälikuid, "Kaashäälikud": kaashäälikuid, "Muud": muid}
