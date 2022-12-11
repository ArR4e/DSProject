def erinevad_sümbolid(sõne):
    hulk = set()
    for sümbol in sõne:
        hulk.add(sümbol)
    return hulk

def sümbolite_sagedus(sõne):
    hulk = {}
    for sümbol in erinevad_sümbolid(sõne):
        hulk[sümbol] = sõne.count(sümbol)
    return hulk
def grupeeri(sõne):
    hulk = {"Täishäälikud": set(),"Kaashäälikud": set(), "Muud": set()}
    täishäälikud = "aeiouõäöüAEIOUÕÄÖÜ"
    kaashäälikud = "xwycjlmnrvkptgbdfhsšzžqJLMNRVKPTGBDFGSŠZŽHQCYWX"
    for el in sümbolite_sagedus(sõne):
        if el in täishäälikud:
            hulk["Täishäälikud"].add((el,sümbolite_sagedus(sõne)[el]))
        elif el in kaashäälikud:
            hulk["Kaashäälikud"].add((el,sümbolite_sagedus(sõne)[el]))
        else:
            hulk["Muud"].add((el,sümbolite_sagedus(sõne)[el]))
    return hulk