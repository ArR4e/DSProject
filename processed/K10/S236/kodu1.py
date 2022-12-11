#Teksti analüüs

sõne = "hulk ei sisalda kunagi korduvaid elemente"

def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk


sõnastik = {}

def sümbolite_sagedus(sõne):
    hulk = set(sõne)
    for sümbol in hulk:
        return sümbol
    
    
def grupeeri(sõne):
    sõnastik['täishäälik'] = set()
    sõnastik['kaashäälik'] = set()
    sõnastik['sümbol'] = set()
    
    