from math import *

def koogi_hind(kook, mõõt):
   if kook == 'šokolaadikook':
       S = pi * mõõt**2
       hind = S * 0.06
       return round(hind, 2)
    
   elif kook == 'ploomikook':
        S = pi*mõõt**2
        hind = S* 0.04
        return round(hind, 2)
    
   elif kook == 'Napoleoni kook':
        S = mõõt**2
        hind = S * 0.1
        return round(hind, 2)
   else:
        raise Exception('Sellist kooki andmebaasist ei leitud.')

while True:
    
    kook = input('Mis on soovitud koogi nimi? ')
    if kook == '':
        break
    mõõt = float(input('Mis mõõduga kooki soovite? '))
    #koogi_hind(kook,mõõt)

    print('Koogi hind on ', koogi_hind(kook,mõõt), ' eurot')
