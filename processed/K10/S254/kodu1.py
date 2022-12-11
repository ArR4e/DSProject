def erinevad_sümbolid(sõne):
    return set(sõne)

# print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(sõne):
    sõnastik = {}
    loendus = 0
    for täht in sõne:
        sõnastik[täht] = sõnastik.get(täht, 0) + 1
#         if täht in sõnastik:
#             sõnastik[täht] = sõnastik[täht] +1
#         else:
#             sõnastik[täht] = 1
    return sõnastik

# print(sümbolite_sagedus("Hei hopsti, väikevend!"))
    
def grupeeri(sõne):
    sõnastik = {}
    sõnastik['Täishäälikud'] = set()
    sõnastik['Kaashäälikud'] = set()
    sõnastik['Muud'] = set()
    for võti,väärtus in sümbolite_sagedus(sõne).items():
        if võti in 'AaEeIiOoUuÕõÄäÖöÜü':
            sõnastik['Täishäälikud'].add((võti,väärtus))
        elif võti in 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsŠšZzŽžTtVvWwXxYy':
            sõnastik['Kaashäälikud'].add((võti,väärtus))
        else:
            sõnastik['Muud'].add((võti,väärtus))
    return sõnastik

print(grupeeri("sõida tasa üle silla"))