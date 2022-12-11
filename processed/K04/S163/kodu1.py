# šokolaadikook (0,06 €/cm2), ploomikook (0,04 €/cm2) ja Napoleoni kook (0,10 €/cm2)
# Šokolaadikook ja ploomikook on ringikujulised
# Napoleoni kook on ruudukujuline
from math import pi

koogid = ["šokolaadikook", "ploomikook", "Napoleoni kook"]

def koogi_hind(kook, mõõt):
    if kook not in koogid:
        raise Exception('Sellist kooki ei leitud.')    
    elif kook == "šokolaadikook":
        pindala = mõõt**2 * pi
        hind = pindala * 0.06
    elif kook == "Napoleoni kook":
        pindala = mõõt**2
        hind = pindala * 0.1
    else:
        pindala = mõõt**2 * pi
        hind = pindala * 0.04
         
    return round(hind, 2)

while True:
    nimi = str(input('Sisesta koogi nimi: '))
    
    if nimi == '':
        print('Lõpp.')
        break
    
    mõõt = float(input('Sisesta koogi mõõt: '))
    
    print(koogi_hind(nimi, mõõt))