def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk

def sümbolite_sagedus(sõne):
    järjend = list(sõne)
    sagedus = {}
    for täht in järjend:
         sagedus[täht] = sagedus.get(täht, 0) + 1
    return sagedus

def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk

def sümbolite_sagedus(sõne):
    järjend = list(sõne)
    sagedus = {}
    for täht in järjend:
         sagedus[täht] = sagedus.get(täht, 0) + 1
    return sagedus

def grupeeri(sõne):
    täishäälikud = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü', 'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü']
    kaashäälikud = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'q', 'y','x', 'w', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    sõnastik = {}
    sõnastik['Täishäälikud'] = set()
    sõnastik['Kaashäälikud'] = set()
    sõnastik['Muud'] = set()
    
    sagedus = sümbolite_sagedus(sõne)
    for täht, kord in sagedus.items():
        ennik = (täht, kord)
        if täht in täishäälikud:
            sõnastik['Täishäälikud'].add(ennik)
        elif täht in kaashäälikud:
            sõnastik['Kaashäälikud'].add(ennik)
        else:
            sõnastik['Muud'].add(ennik)
           
    return sõnastik
          
        
    