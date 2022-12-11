def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk

def sümbolite_sagedus(sõne):
    d = {}
    for märk in sõne:
        d[märk] = d.get(märk, 0) +1
    return d

def grupeeri(sõne):
    d = {}
    täishäälikud = "euioüõaöäEUIOÜÕAÖÄ"
    kaashäälikud = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsŠšZzŽžTtVvWwXxYy"
    täish_sõne = ""
    kaash_sõne = ""
    muu = ""
    for märk in sõne:
        if märk in täishäälikud:
            täish_sõne += märk
        elif märk in kaashäälikud:
            kaash_sõne += märk
        else:
            muu += märk
    t = set(sümbolite_sagedus(täish_sõne).items())
    k = set(sümbolite_sagedus(kaash_sõne).items())
    m = set(sümbolite_sagedus(muu).items())
    d["Täishäälikud"] = t
    d["Kaashäälikud"] = k
    d["Muud"] = m
    return d

