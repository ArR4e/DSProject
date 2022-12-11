import string

def erinevad_sümbolid(sõne):
    return(set(sõne))
#print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for i in sõne:
        if i in sõnastik:
            sõnastik[i] += 1
        elif i not in sõnastik:
            sõnastik[i] = 1
    return(sõnastik)
#print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(sõne):
    kaas = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsŠšZzŽžTtVvWwXxYy"
    täis = "aeiouõäöüAEIOUÕÄÖÜ"
    sümbolid = string.punctuation + " "
    sõnastik = {}
    täishäälikud = {}
    kaashäälikud = {}
    muud = {}
    täisset = set()
    kaasset = set()
    muudset = set()
    for i in sõne:
        if i in täis:
            if i in täishäälikud:
                täishäälikud[i] += 1
            elif i not in täishäälikud:
                täishäälikud[i] = 1
        elif i in kaas:
            if i in kaashäälikud:
                kaashäälikud[i] += 1
            elif i not in kaashäälikud:
                kaashäälikud[i] = 1
        elif i in sümbolid:
            if i in muud:
                muud[i] += 1
            elif i not in muud:
                muud[i] = 1
    for i in kaashäälikud:
        kaasset.add((i, kaashäälikud.get(i)))
    for i in täishäälikud:
        täisset.add((i, täishäälikud.get(i)))
    for i in muud:
        muudset.add((i, muud.get(i)))
    sõnastik["Täishäälikud"] = täisset
    sõnastik["Kaashäälikud"] = kaasset
    sõnastik["Muud"] = muudset
    return(sõnastik)
#print(grupeeri("sõida tasa üle silla"))
