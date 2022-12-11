from math import pi
def koogi_hind(a, b):
    if a == 'šokolaadikook':
        pindala = pi * (b**2)
        hind = float(0.06)
        print('Koogitüki hind on: ', round(pindala * hind, 2))
    elif a == 'ploomikook':
        pindala = pi * (b**2)
        hind = float(0.04)
        print('Koogitüki hind on: ', round(pindala * hind, 2))
    elif a == 'Napoleoni kook':
        pindala = b**2
        hind = float(0.10)
        print('Koogitüki hind on: ', round(pindala * hind, 2))
    else:
        print("Sellist kooki andmebaasist ei leitud")



while True:
    a = input('Sisestage kooginimi')
    b = float(input('Sisestage külje või raadiuse mööde(cm)'))
    koogi_hind(a, b)
    
    if a == '':
        break
    