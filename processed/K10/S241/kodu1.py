# 1
#Kirjuta funktsioon erinevad_sümbolid, mis võtab argumendiks sõne ning tagastab kõigi antud sõnes leiduvate erinevate sümbolite hulga.
# 
# >>> erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente")
# {'h', 'e', 'r', 'v', 'l', 'k', 'i', 'g', 't', 'd', 's', 'u', 'a', ' ', 'm', 'o', 'n'}

a='aias sadas saia, nõnda arvas Kaia, tulles väravast läbi, mööda teed laia'
def erinevad_sümbolid(sõne):
    sõne_hulk = set(sõne)
    return sõne_hulk
print(erinevad_sümbolid(a))

# 2
# Seejärel kirjuta funktsioon sümbolite_sagedus, mis võtab argumendiks sõne ja tagastab sõnastiku,
# mille kirjeteks on sõnes sisalduvad tähed koos nende esinemissagedustega. Sõnastiku võtmeteks peaksid olema tähed või
# muud sümbolid (st tehniliselt võttes sõned) ja väärtusteks täisarvud.
# 
# >>> sümbolite_sagedus("Hei hopsti, väikevend!")
# {'H': 1, 'e': 3, 'i': 3, ' ': 2, 'h': 1, 'o': 1, 'p': 1, 's': 1, 't': 1, ',': 1, 'v': 2, 'ä': 1, 'k': 1, 'n': 1, 'd': 1, '!': 1}

sõnastik ={}
def sümbolite_sagedus(sõne):
    for el in list(sõne):
        sõnastik[el] = sõnastik.get(el, 0) + 1
    return sõnastik
print(sümbolite_sagedus(a))

# 3
# Loo funktsioon grupeeri, mis võtab argumendiks sõne ja tagastab sõnastiku, kus on kolm võtit: täishäälikud, kaashäälikud ja
# muud sümbolid (st kirjavahemärgid ja tühikud). Iga võtme väärtuseks on vastavat tüüpi häälikute ning esinemissageduste paaride hulk.
# 
# >>> grupeeri("sõida tasa üle silla")
# {'Täishäälikud': {('a', 4), ('e', 1), ('i', 2), ('õ', 1), ('ü', 1)}, 'Kaashäälikud': {('d', 1), ('l', 3), ('t', 1), ('s', 3)},
# 'Muud': {(' ', 3)}}

vokaalid = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü', 'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü']
konsonandid = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'z', 't', 'v', 'B', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'Z', 'T', 'V']
märgid = ['.', ',', ' ', '!', '?', ';', ':']
sõne_järjend_v =[]
sõne_järjend_k =[]
sõne_järjend_m =[]
sõnastik_v = {}
sõnastik_k ={}
sõnastik_m = {}
def grupeeri(sõne):
    sõne_järjend = list(sõne)
    for el in sõne_järjend:
        if el in vokaalid:
            sõne_järjend_v.append(el)
            for el_v in sõne_järjend_v:
                sõnastik_v[el_v] = sõnastik_v.get(el_v, 0) + 1
        if el in konsonandid:
            sõne_järjend_k.append(el)
            for el_k in sõne_järjend_k:
                sõnastik_k[el_k] = sõnastik_k.get(el_k, 0) + 1
        if el in märgid:
            sõne_järjend_m.append(el)
            for el_m in sõne_järjend_m:
                sõnastik_m[el_m] = sõnastik_m.get(el_m, 0) + 1
    return ("Vokaalid: ",  sõnastik_v, "Konsonandid: ",  sõnastik_k, "Märgid: ",  sõnastik_m)

print(grupeeri(a))