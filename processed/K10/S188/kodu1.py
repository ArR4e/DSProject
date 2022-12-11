def erinevad_sümbolid(sõne):
    sümbolite_hulk = set()
    for i in sõne:
        sümbolite_hulk.add(i)
    return sümbolite_hulk

def sümbolite_sagedus(sõne):
    sümboli_sõnastik = {}
    for i in sõne:
        sümboli_sõnastik[i] = sõne.count(i)
    return sümboli_sõnastik

def grupeeri(sõne):
    täishäälikud = "aeiouõäöüAEIOUÕÄÜI"
    kaashäälikud = "bdfghjklmnprsšzžtvcxqywBDFGHJKLMNPRSŠZŽTVCXQYW"
    hulk_täish = set()
    hulk_kaash = set()
    hulk_muud = set()
    grupeering = {}
    sümbolite_esinemine = sümbolite_sagedus(sõne)
    for i in erinevad_sümbolid(sõne):
        if i in täishäälikud:
            hulk_täish.add((i, sümbolite_esinemine[i]))
        elif i in kaashäälikud:
            hulk_kaash.add((i, sümbolite_esinemine[i]))
        else:
            hulk_muud.add((i, sümbolite_esinemine[i]))
    grupeering["Täishäälikud"] = hulk_täish
    grupeering["Kaashäälikud"] = hulk_kaash
    grupeering["Muud"] = hulk_muud
    return grupeering
