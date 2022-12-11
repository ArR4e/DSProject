import math

def koogi_hind(koogi_nimi, koogi_mõõt):
    if koogi_nimi.lower() == "šokolaadikook":
        koogi_pindala = pow(koogi_mõõt, 2) * math.pi
        koogi_hind = koogi_pindala * 0.06
        return round(koogi_hind,2)
    elif koogi_nimi.lower() == "ploomikook":
        koogi_pindala = pow(koogi_mõõt, 2) * math.pi
        koogi_hind = koogi_pindala * 0.04
        return round(koogi_hind,2)
    elif koogi_nimi.lower() == "napoleoni kook":
        koogi_pindala = pow(koogi_mõõt, 2)
        koogi_hind = koogi_pindala * 0.10
        return round(koogi_hind,2)
    else:
         raise Exception("Sellist kooki andmebaasist ei leitud")

koogid_nimelist = []
koogid_mõõdud = []

while True:
    koogi_nimi = input("Sisestage koogi nimi: ")
    if koogi_nimi == "":
        break
    koogid_nimelist.append(koogi_nimi)
    koogid_mõõdud.append(input("Sisestage koogi mõõt: "))

i = 0
for koogi_nimi in koogid_nimelist:
    try:
        print("Koogi hind on ", koogi_hind(koogi_nimi, float(koogid_mõõdud[i])), " eurot")
    except:
        print("Sellist kooki andmebaasist ei leitud")

    i += 1
