# 1. Teksti analüüs

import string

def erinevad_sümbolid(sõne):
    b = list(sõne)
    vastus = set(b)
    return vastus

def sümbolite_sagedus(sõne):
    b = list(sõne)
    sõnastik = {}
    for i in b:
        try:
            if sõnastik[i] >= 1:
                sõnastik[i] = sõnastik[i] + 1
        except:    
            sõnastik[i] = 1
    vastus = sõnastik
    return vastus    
    
def grupeeri(sõne):
    sõnastik = sümbolite_sagedus(sõne)
    vastus = {}
    vastus['Täishäälikud'] = set()
    vastus['Kaashäälikud'] = set()
    vastus['Muud'] = set()
    for i in sõnastik:
        if i in 'AEIOUÕÖÄÜaeiouõöäü':
            vastus['Täishäälikud'].add((i, sõnastik[i]))
        elif i in 'BCDFGHJKLMNPQRSŠZŽTVWXYbcdfghjklmnpqrsšzžtvwxy':    
            vastus['Kaashäälikud'].add((i, sõnastik[i]))
        elif i in ' ' + string.punctuation:
            vastus['Muud'].add((i, sõnastik[i]))
    return vastus

#sõne = "hulk ei sisalda kunagi korduvaid elemente"
#vastus = erinevad_sümbolid(sõne)
#print(vastus)

#sõne = "Hei hopsti, väikevend!"
#vastus = sümbolite_sagedus(sõne)
#print(vastus)

#sõne = "sõida tasa üle silla"
#vastus = grupeeri(sõne)
#print(vastus)