def erinevad_sümbolid(tekst):
    return set(tekst)

def sümbolite_sagedus(tekst):
    d = dict.fromkeys(erinevad_sümbolid(tekst), 0)
    for i in tekst:
        if i in d:
            d[i] += 1
    return d
            
def grupeeri(tekst):
    d = {"Täishäälikud": set(),
         "Kaashäälikud": set(),
         "Muud": set()}
    a = sümbolite_sagedus(tekst)
    
    for i in a:
        if i in "iüueöõoäaIÜUEÖÕOÄA":
            d["Täishäälikud"].add((i,a[i]))
        elif i in "bcdfghjklmnpqrsšzžtvwxyBCDFGHJKLMNPQRSŠZŽTVWXY":
            d["Kaashäälikud"].add((i,a[i]))
        else:
            d["Muud"].add((i,a[i]))
    return d