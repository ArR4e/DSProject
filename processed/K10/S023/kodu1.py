


def erinevad_sümbolid(a):
    k = set()
    for i in a:
        if i not in k:
            k.add(i)
        else:
            continue
    return k

def sümbolite_sagedus(a):
    k = {}
    for i in a:
        if i not in k:
            k[i] = 0
            k[i] = k[i] + 1
        else:
            k[i] = k[i] + 1
    return k

def grupeeri(a):
    täishäälikud = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
    kaashäälikud = ["b","d","f","g","h","j","k","l","m","n","p","r","s","š","z","ž","t","v","c"]
    
    k = sümbolite_sagedus(a)
    t = {}
    t["täishäälikud"] = ()
    t["kaashäälikud"] = ()
    t["muud"] = ()
    for i in k:
        if i in täishäälikud:
            t["täishäälikud"] =t["täishäälikud"]  + ((i,k[i]))
        elif i in kaashäälikud:
            t["kaashäälikud"] = t["kaashäälikud"] + ((i,k[i]))
        else:
            t["muud"] = t["muud"] + ((i,k[i]))
    return t
print(grupeeri("sõida tasa üle silla"))
    