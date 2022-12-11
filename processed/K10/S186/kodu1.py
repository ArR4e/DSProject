def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sõnastik={}
    for el in sõne:
        esinemissagedus=sõne.count(el)
        sõnastik[el]=esinemissagedus
    return sõnastik

def grupeeri(sõne):
    sõnastik={}
    täishäälikud=['a', ]
    kaashäälikud=[]
    muu=[]
    for el in sõne:
        if el in täishäälikud:
            esinemissagedus=sõne.count(el)
            täishäälikud[el]=esinemissagedus
        elif el in kaashäälikud:
            esinemissagedus=sõne.count(el)
            kaashäälikud[el]=esinemissagedus
        elif el in muu:
            esinemissagedus=sõne.count(el)
            muu[el]=esinemissagedus

