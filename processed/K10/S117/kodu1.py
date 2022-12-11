#alustasin 30.10.2021 (21:30)
def erinevad_sümbolid(sõne):
    sõne = set(sõne)
    return sõne

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for i in sõne:
        if i not in sõnastik:
            sõnastik[i] = 1
        else:
            sõnastik[i] += 1
    return sõnastik

def grupeeri(sõne):
    sõnastik = {}
    sõnastik['Täishäälikud'] = set()
    sõnastik['Kaashäälikud'] = set()
    sõnastik['Muud'] = set()
    sagedus = sümbolite_sagedus(sõne)
    for i in sagedus.items():
        sumbol1 = i[0]
        sumbol2 = sumbol1.lower()
        if sumbol2 in "aeiouõäöü":
            sõnastik['Täishäälikud'].add(i)
        elif sumbol2 in "bcdfghjklmnprsšžztvxqwy":
            sõnastik['Kaashäälikud'].add(i)
        else:
            sõnastik['Muud'].add(i)
    return sõnastik