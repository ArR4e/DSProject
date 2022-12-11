def erinevad_sümbolid(sõne1):
    s = set()
    hulk1 = set(sõne1)
    for el in hulk1:
        s.add(el)
    return s
        
def sümbolite_sagedus(sõne2):
    sõnastik = {}
    for täht in sõne2:
        sõnastik[täht] = sõnastik.get(täht, 0) + 1
    return sõnastik

def grupeeri(sõne3):
    sõnastik1 = {}
    sõnastik1["Täishäälikud"] = set()
    sõnastik1["Kaashäälikud"] = set()
    sõnastik1["Muud"] = set()
    x = sümbolite_sagedus(sõne3)
    täishäälikud = "AEIOUÄÕÜÖaeiouõäöü"
    kaashäälikud = "BCDFGHJKLMNPRSŠZŽTVWXYQbcdfghjklmnprsšzžtvwxqy"
    for häälik in x:
        if häälik in täishäälikud:
            ennik = (häälik, x.get(häälik))
            sõnastik1["Täishäälikud"].add(ennik)
        elif häälik in kaashäälikud:
            ennik2 = (häälik, x.get(häälik))
            sõnastik1["Kaashäälikud"].add(ennik2)
        else:
            ennik3 = (häälik, x.get(häälik))
            sõnastik1["Muud"].add(ennik3)
    return sõnastik1