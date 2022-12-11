'''-- Kodutöö nr. 10 - 1. Teksti analüüs --'''
'''Funktsioon 'erinevad_sümbolid' võtab argumendiks sõne ning tagastab kõigi antud sõnes leiduvate erinevate sümbolite hulga.
   Funktsioon 'sümbolite_sagedus' võtab argumendiks sõne ja tagastab sõnastiku, mille kirjeteks on tähed koos nende esinemissagedustega.
   Funktsioon 'grupeeri' võtab argumendiks sõne ja tagastab sõnastiku, kus on kolm võtit:
   täishäälikud, kaashäälikud ja muud sümbolid. Iga võtme väärtuseks on vastavat tüüpi häälikute ning esinemissageduste paaride hulk.'''
########################################################################################################################################
def erinevad_sümbolid(sõne):
    return set(sõne)
########################################################################################################################################
def sümbolite_sagedus(sõne):
    # tagastatav sõnastik
    sagedused = {}
    
    for s in sõne:
        if not (s in sagedused):
            sagedused[s] = sõne.count(s)
    
    return sagedused
########################################################################################################################################
def grupeeri(sõne):
    # tagastatav sõnastik
    grupeeritud = {}
    
    # tagastatavad sümbolite hulgad
    täishäälikud = set()
    kaashäälikud = set()
    muud = set()
    
    for s in sõne:
        num = sõne.count(s)
        if s in 'aeiouõäöü' or s in 'aeiouõäöü'.upper():
            täishäälikud.add((s, num))
        elif s in 'jlmnrvszhfšžkgpqbctdwxy' or s in 'jlmnrvszhfšžkgpqbctdwxy'.upper():
            kaashäälikud.add((s, num))
        else:
            muud.add((s, num))
    
    grupeeritud['Täishäälikud'] = täishäälikud
    grupeeritud['Kaashäälikud'] = kaashäälikud
    grupeeritud['Muud'] = muud
    
    return grupeeritud
########################################################################################################################################
print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))
print(sümbolite_sagedus("Hei hopsti, väikevend!"))
print(grupeeri("sõida tasa üle silla"))
print(grupeeri("'Kuule, August! Käes on august?' küsis August ühest august. 'Lõppend august!' vastas August teisest august."))