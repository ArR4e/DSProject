def erinevad_sümbolid(a):
    asi = []
    for el in word:
        asi.append(el)
    return asi

def sümbolite_sagedus(b):
    symbol = erinevad_sümbolid(b)
    sagedus = []
    for char in b:
        number = str(b.count(symbol))
        sagedus.append(""+symbol+":"+number)
    sagedus = list(dict.fromkeys(sagedus))
    return sagedus

def grupeeri(c):
    sonastik = {}
    sonastik["Täishäälik"] = set()
    sonastik["Kaashäälik"] = set()
    sonastik["Sümbolid"] = set()