def erinevad_sümbolid(sone):
    hulk = set()
    for x in sone:
        if x not in hulk:
            hulk.add(x)
    return hulk

def sümbolite_sagedus(sone):
    sonastik = {}
    jarjend = []
    for x in sone:
        if x not in sonastik:
            
        else:
            sonastik[x] += 1
    return sonastik
