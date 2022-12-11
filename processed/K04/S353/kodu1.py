from math import pi
def koogi_hind(koogi_nimi, mõõt):
    if koogi_nimi!='šokolaadikook' and koogi_nimi!='ploomikook' and koogi_nimi!='Napoleoni kook':
        raise Exception('Sellist kooki andmebaasist ei leitud')
    if koogi_nimi =='šokolaadikook' or koogi_nimi=='ploomikook':
        return mõõt**2*pi
    if koogi_nimi=='Napoleoni kook':
        return mõõt*mõõt
while True:
    
    koogi_nimi=input('Palun sisestage koogi nimi: ')
    if koogi_nimi=='':
        break
    mõõt=float(input('Palun sisetage koogi mõõt: '))
    pindala=koogi_hind(koogi_nimi, mõõt)
    if koogi_nimi=='šokolaadikook':
        print(round(pindala*0.06, 2), '€')
    if koogi_nimi=='ploomikook':
        print(round(pindala*0.04, 2), '€')
    if koogi_nimi=='Napoleoni kook':
        print(round(pindala*0.10, 2), '€')