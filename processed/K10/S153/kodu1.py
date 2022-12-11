def erinevad_sümbolid(sõne):
    sümbolite_hulk = set()
    for el in sõne:
        for i in el:
            if i not in sümbolite_hulk:
                sümbolite_hulk.add(i)
    return sümbolite_hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for el in sõne:
        sõnastik[el] = sõnastik.get(el, 0) + 1
    return sõnastik

def convert(list):
    i = iter(list)
    ld = dict(list)
    return ld

def grupeeri(sõne):
    vokaalid = list("aeiouõäöüAEIOUÕÄÖÜ")
    konsonandid = list("kKlLmMnNpPrRsSšŠzZžŽtTbBdDfFgGhHjJvV")
    muud = list("!?.,#%&/()=[]{}+-_;: 1234567890")
    sõnastiku_list = list(sümbolite_sagedus(sõne).items())
    sõnastik2 = {}
    täishäälikud = []
    kaashäälikud = []
    muu = []
    for el in sõnastiku_list:
        if el[0] in vokaalid:
            täishäälikud.append(el)
            uus = convert(täishäälikud)
            sõnastik2["täishäälikud"] = uus
        elif el[0] in konsonandid:
            kaashäälikud.append(el)
            uus2 = convert(kaashäälikud)
            sõnastik2["kaashäälikud"] = uus2
        elif el[0] in muud:
            muu.append(el)
            uus3 = convert(muu)
            sõnastik2["muud"] = uus3
    return sõnastik2
print(grupeeri("sõida tasa üle silla"))
