
def erinevad_sümbolid(sõne):
    a = set()
    for i in range(len(sõne)):
        if sõne[i] not in a:
            a.add(sõne[i])
    return a
print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(sõne):
    a = {}
    for i in range(len(sõne)):
        if sõne[i] not in a:
            a[sõne[i]] = 1
        else:
            a[sõne[i]] += 1
    return a

print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(sõne):
    a = {"Täishäälikud": set(), "Kaashäälikud": set(), "Muud": set()}
    täis = "aeiouõäöü"
    sagedus = sümbolite_sagedus(sõne)
    for key, value in sagedus.items():
        if key in täis or key in täis.upper():
            a["Täishäälikud"].add((key, value))
        elif key.isalpha():
            a["Kaashäälikud"].add((key, value))
        else:
            a["Muud"].add((key,value))
    return a
        
print(grupeeri("sõida tasa üle silla"))
        
        
        
        