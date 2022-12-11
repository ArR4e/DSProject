def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sõnastik={}
    järjend=list(sõne)
    for el in järjend:
        sõnastik[el]=sõnastik.get(el,0)+1
    return sõnastik

def grupeeri(sõne):
    sõnastik={}
    sõnastik["Täishäälikud"]=set()
    sõnastik["Kaashäälikud"]=set()
    sõnastik["Muud"]=set()
    sagedus=sümbolite_sagedus(sõne)
    for võti in sagedus:
        ennik=(võti,sagedus[võti]) 
        if võti in "aeiouõäöüAEIOUÕÄÖÜ":
            sõnastik["Täishäälikud"].add(ennik)
        elif võti in "bcdfghjklmnpqrsztvwxyBCDFGHJKLMNPQRSZTVWXY":
            sõnastik["Kaashäälikud"].add(ennik)
        else:
            sõnastik["Muud"].add(ennik)
    return sõnastik
        