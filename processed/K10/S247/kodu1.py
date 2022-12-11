def erinevad_sümbolid(s):
    f = set(s)
    return f

d = {}
def sümbolite_sagedus(sõne):
    for täht in sõne:
        d[täht] = d.get(täht, 0) + 1
    return d

def grupeeri(sõne):
    täishäälikud = ["a","e","i","o","u","õ","ä","ö","ü","A","E","I","O","U","Õ","Ä","Ö","Ü"]
    kaashäälikud = ["b","d","f","g","h","j","k","l","m","n","p","r","s","š","z","ž","t","v","c","q","w","y","z","x","B","D","F","G","H","J","K","L","M","N","P","R","S","Š","Z","Ž","T","V","C","Q","W","Y","Z","X"]
    t = {}
    k = {}
    m = {}
    for täht in sõne:
        if täht in täishäälikud:
            t[täht] = t.get(täht, 0) + 1
        elif täht in kaashäälikud:
            k[täht] = k.get(täht, 0) + 1
        else:
            m[täht] = m.get(täht, 0) + 1
    t1 = list(t.items())
    t2 = set(t1)
    
    k1 = list(k.items())
    k2 = set(k1)
    
    m1 = list(m.items())
    m2 = set(m1)
    
    sõnastik = {"Täishäälikud":t2, "Kaashäälikud":k2, "Muud":m2}
    return sõnastik



















      
      
      