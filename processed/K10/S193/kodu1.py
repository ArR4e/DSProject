# sõna = "hello"

def erinevad_sümbolid(sõne):
    return set(sõne)


def sümbolite_sagedus(sõne):
    sõnastik = {}
    for el in sõne:
        if el in sõnastik:
            sõnastik[el] = sõnastik[el] + 1
        else:
            sõnastik[el] = 1
    return sõnastik



    
