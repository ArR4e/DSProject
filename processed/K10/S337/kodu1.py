def erinevad_sümbolid(sõne):
    return set(sõne)
def sümbolite_sagedus(sõne):
    sõnastik = {}
    for täht in sõne:
        sõnastik[täht] = sõnastik.get(täht, 0) + 1
    return sõnastik
def grupeeri(sõne):
    vokaalid = ['A', 'E', 'I', 'O', 'U', 'Ü', 'Õ', 'Ö', 'Ä']
    konsonandid = ['B', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'C', 'Q', 'Z', 'Š', 'Ž'] 
    sõnastik = sümbolite_sagedus(sõne)
    täishäälikud = set()
    kaashäälikud = set()
    muud = set()
    for el in sõnastik.items():
        if el[0].upper() in vokaalid:
            täishäälikud.add(el)
        elif el[0].upper() in konsonandid:
            kaashäälikud.add(el)
        else:
            muud.add(el)
    vastus = {'Täishäälikud': täishäälikud, 'Kaashäälikud': kaashäälikud, 'Muud': muud}
    return vastus          
            
    