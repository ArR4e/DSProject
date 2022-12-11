# teksti analüüs


def erinevad_sümbolid(sõne):
    return set(sõne)


def sümbolite_sagedus(sõne):
    d = {}
    for char in sõne:
        d[char] = sõne.count(char)
    return d


def grupeeri(sõne):
    if sõne == "":
        return
    
    t_häälik = "a e i o u õ ä ö ü".split()
    k_häälik = "b d f g h i j k l m n p r s š z ž t v w q y c x".split()
    d = {}
    kaashäälikud = set()
    täishäälikud = set()
    muu = set()

    for char in sõne:
        x = (char, sõne.count(char))

        if char.lower() in t_häälik:
            täishäälikud.add(x)
        elif char.lower() in k_häälik:
            kaashäälikud.add(x)
        else:
            muu.add(x)

        d["Täishäälikud"] = täishäälikud
        d["Kaashäälikud"] = kaashäälikud
        d["Muud"] = muu

    return d
