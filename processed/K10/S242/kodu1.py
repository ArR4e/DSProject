sümbolid = set()
def erinevad_sümbolid(sõne):
    for täht in sõne:
        sümbolid.add(täht)
    return sümbolid


def sümbolite_sagedus(sõne):
    sümbolid = []
    for täht in sõne:
        sümbolid.append(täht)
    sagedus = {}
    for täht in sümbolid:
        if täht in sagedus:
            sagedus[täht] = sagedus[täht] + 1
        else:
            sagedus[täht] = 1
    return sagedus

def grupeeri(sõne):
    sõne = sümbolite_sagedus(sõne).items()
    sõnastik = {'Täishäälikud': set(), 'Kaashäälikud': set(), 'Muud': set()}
    täishäälikud = ['a', 'e', 'u', 'i', 'o', 'ü', 'õ', 'ä', 'ö', 'A', 'E', 'U', 'I', 'O', 'Ü', 'Õ', 'Ä', 'Ö']
    kaashäälikud = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'R', 'T', 'Y', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    for täht, kordus in sõne:
        paar = (täht, kordus)
        if täht in täishäälikud:
            sõnastik['Täishäälikud'].add(paar)
        elif täht in kaashäälikud:
            sõnastik['Kaashäälikud'].add(paar)
        else:
            sõnastik['Muud'].add(paar)
    return sõnastik


        

