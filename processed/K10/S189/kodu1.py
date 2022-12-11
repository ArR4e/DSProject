def erinevad_sümbolid(sõne):
    tühi = set()
    for i in sõne:
        tühi.add(i)
    return(tühi)
#print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(sõne):
    tühi = {}
    for i in sõne:
        if i in tühi:
            tühi[i] += 1
        else:
            tühi[i] = 1
    return(tühi)
print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(sõne):
    tühi = {}
    tühi["Täishäälikud"] = set()
    tühi["Kaashäälikud"] = set()
    tühi["Muud"] = set()
    for i in sõne:
        if i in "aeiouõäöüAEIOUÕÄÖÜ":
            tühi["Täishäälikud"].add((i, sõne.count(i)))
        elif i in "vcwxyzqjlmnrshfšzžgkbpdtVCWXYZQJLMNRSHFŠZŽGKBPDT":
            tühi["Kaashäälikud"].add((i, sõne.count(i)))
        else:
            tühi["Muud"].add((i, sõne.count(i)))
    return(tühi)
   
#print(grupeeri(("Hei hopsti, väikevend!")))
#print(grupeeri(("sõida tasa üle silla")))