def erinevad_sümbolid(a) :
    hulk = set()
    for el in a:
        hulk.add(el)
    return hulk

sõnastik1 = {}
def sümbolite_sagedus(b) :
    for i in b:
        if i in sõnastik1:
            sõnastik1[i.lower()] = sõnastik1[i] + 1
        else:
            sõnastik1[i.lower()] = 1
    return(sõnastik1)

def grupeeri(b) :
    sõnastik2 = sümbolite_sagedus(b)
    d = {}
    kaas_häälikud = set()
    täis_häälikud = set()
    muud = set()
    Kaashäälikud = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    Täishäälikud = ["a","e","i","o","u","õ","ä","ö","ü"]
    for j in sõnastik2.keys():
        e = (j, sõnastik2[j])
        if j in Kaashäälikud:
            kaas_häälikud.add(e)
        elif j in Täishäälikud:
            täis_häälikud.add(e)
        else:
            muud.add(e)
    d["Kaashäälikud"] = kaas_häälikud
    d["Täishäälikud"] = täis_häälikud
    d["Muu"] = muud
    return(d)