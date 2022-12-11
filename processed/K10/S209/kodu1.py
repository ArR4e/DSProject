#Viimast funktsiooni ei saanud päris tööle
hulk = set()
sonastik = {}
sonastik2 = {}
sonastik2["Täishäälik"] = set()
sonastik2["Kaashäälik"] = set()
sonastik2["Muu"] = set()
def erinevad(sone):

    for el in sone:
        hulk.add(el)
    return hulk


def sagedus(sone):
    for el in sone:
        if el in sonastik:
            sonastik[el] += 1
        else:
            sonastik[el] = 1
    return sonastik

def grupeeri(sone):
    
    
    return sonastik2


print(erinevad("hulk ei sisalda kunagi korduvaid elemente"))
print(sagedus("Hei hopsti, väikevend!"))