def erinevad_sümbolid(sõne):
    tähed = []
    for täht in sõne:
        tähed += täht
    hulk = set(tähed)
    return hulk

def sümbolite_sagedus(sõne):
    d = {}
    for täht in sõne:
        if täht in d:
            d[täht] = d[täht] + 1
        else:
            d[täht] = 1
    return d

def grupeeri(sõne):
    täishäälikud = {"a","e","i","o","u","õ","ä","ö","ü"}
    kaashäälikud = {"l","m","n","r","s","h","v","j","k","g","p","b","t","d"}
    
# x = thisdict.get("model")
    
    d = sümbolite_sagedus(sõne)
    täis = set()
    kaas = set()
    muud = set()

    for sümbol in d:
        if sümbol in täishäälikud:
            a = (sümbol, d[sümbol])
            täis.add(a)
        if sümbol in kaashäälikud:
            b = (sümbol, d[sümbol])
            kaas.add(b)
        if sümbol not in täishäälikud and sümbol not in kaashäälikud:
            c = (sümbol, d[sümbol])
            muud.add(c)
    grupeeritud = {
        "Täishäälikud": täis,
        "Kaashäälikud": kaas,
        "Muud": muud
        }
    return grupeeritud
grupeeri("sõida tasa üle silla")