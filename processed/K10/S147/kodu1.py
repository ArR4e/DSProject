täishäälikud = {"a","e","i","o","u","õ","ä","ö","ü"}
kaashäälikud = {"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"}
def erinevad_sümbolid(sõne):
    hulk = set()
    for i in sõne:
        hulk.add(i)
    return hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for i in sõne:
        sõnastik[i] = sõnastik.get(i,0)+1
    return sõnastik

def grupeeri(sõne):
    sõnastik = list(sümbolite_sagedus(sõne).items())
    täis = set()
    kaas = set()
    muud = set()
    for i in sõnastik:
        temp = i[0].lower()
        if temp in täishäälikud: täis.add(i)
        elif temp in kaashäälikud: kaas.add(i)
        else: muud.add(i)
    grupeeritud = {"Täishäälikud":täis,"Kaashäälikud":kaas,"Muud":muud}
    return grupeeritud