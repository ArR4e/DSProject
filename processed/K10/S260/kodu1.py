def erinevad_sümbolid(s):
    return set(s)

def sümbolite_sagedus(s):
    d = {}
    unq_symb = erinevad_sümbolid(s)
    for täht in unq_symb:
        d[täht] = s.count(täht)
    return d

def grupeeri(s):
    group = {"Täishäälikud":set(),"Kaashäälikud":set(),"Muud":set()}
    täishäälikud = ["a","e","i","o","u","õ","ä","ö","ü","A","E","I","O","U","Õ","Ä","Ö","Ü"]
    kaashäälikud = ["b","d","f","g","h","j","k","l","m","n","p","r","s","t","v","B","D","F","G","H","J","K","L","M","N","P","R","S","T","V","W","w","C","c","Z","z","q","Q","Y","y","š","ž","Ž","Š","x","X"]
    frq_symb = sümbolite_sagedus(s)
    for täht in frq_symb.keys():
        if täht in täishäälikud:
            group["Täishäälikud"].add((täht, frq_symb[täht]))
        elif täht in kaashäälikud:
            group["Kaashäälikud"].add((täht, frq_symb[täht]))
        else:
            group["Muud"].add((täht, frq_symb[täht]))
    return group

grupeeri("a cöd")