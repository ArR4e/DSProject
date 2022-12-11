def erinevad_sümbolid(sõne):
    hulk = set()
    for i in sõne:
        if i not in hulk:
            hulk.add(i)
    return hulk
def sümbolite_sagedus(sõne):
    sõnastik = {}
    for täht in sõne:
        sõnastik[täht] = sõne.count(täht)
    return sõnastik
def grupeeri(sõne):
    täishäälikud = ["a", "e", "i", "o", "u","õ", "ä","ö", "ü"]
    kaashäälikud = ["b","d","g","h","j","k","l","m","n","p","r","s","t","v"]
    sõnastik = {}
    kaashäälik = ""
    täishäälik = ""
    muu = ""
    for i in sõne:
        if i.lower() in kaashäälikud:
            kaashäälik += i
        elif i.lower() in täishäälikud:
            täishäälik += i
        else:
            muu += i
    sõnastik["Täishäälikud"] = set(sümbolite_sagedus(täishäälik))
    sõnastik["Kaashäälikud"] = set(sümbolite_sagedus(kaashäälik))
    sõnastik["Muud"] = sümbolite_sagedus(muu)
    return sõnastik