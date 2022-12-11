def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for täht in sõne:
        if täht in sõnastik:
            sõnastik[täht] += 1
        else:
            sõnastik[täht] = 1
    return sõnastik

def grupeeri(sõne):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    
    täishäälikud = "aeiouõäöüAEIOUÕÄÖÜ"
    kaashäälikud = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    tegevus = sümbolite_sagedus(sõne)
    
    for täht in tegevus:
        võti = tegevus.get(täht)
        element = (str(täht), võti)
        if täht in täishäälikud:
            sõnastik["Täishäälikud"].add(element)
        elif täht in kaashäälikud:
            sõnastik["Kaashäälikud"].add(element)
        else:
            sõnastik["Muud"].add(element)
    return sõnastik