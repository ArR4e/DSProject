#Pagarikoja kassaaparaat
#šokolaadikook (0,06 €/cm**2) - ring
#ploomikook (0,04 €/cm**2) - ring
#Napoleoni kook (0,10 €/cm**2) - ruut
from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        maksumus = 0.06*(pi*mõõt**2)
    elif nimi == "ploomikook":
        maksumus = 0.04*(pi*mõõt**2)
    elif nimi == "Napoleoni kook":
        maksumus = 0.1*(mõõt**2)
    else:
        print("Sellist kooki andmebaasist ei leitud.")
    maksumus = round(maksumus, 2)
    return maksumus

kogu_maksumus = 0
while True:
    koogi_nimi = input("Sisesta koogi nimi: ")
    if koogi_nimi == "":
        break
    koogi_mõõt = input("Sisesta koogi mõõt (cm): ")
    if koogi_mõõt == "":
        break
    koogi_mõõt = float(koogi_mõõt )
    print(koogi_hind(koogi_nimi, koogi_mõõt))
