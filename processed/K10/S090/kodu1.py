def erinevad_sümbolid(x):
    h = set(x)
    return h

def sümbolite_sagedus(y):
    d ={}
    for i in y:
        d[i] = d.get(i, 0) + 1
    return d

def grupeeri(z):
    d = {}
    täishäälik = ["a","e","i","o","u","õ","ä","ö","ü"]
    kaashäälik = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","š","z","ž","t","v","w","x","y"]
    t = set()
    k = set()
    m = set()
    s = sümbolite_sagedus(z)
    for i in s:
        if i.lower() in täishäälik:
            t.add((i, s[i]))
        elif i.lower() in kaashäälik:
            k.add((i, s[i]))
        else:
            m.add((i, s[i]))
    d["Täishäälikud"] = t
    d["Kaashäälikud"] = k
    d["Muud"] = m
    return d
        

        
    
        
    
        