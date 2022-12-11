from math import *

a = input('Sisestage torti nimi:')
b = int(input('Sisestage torti suurus:'))
def koogi_hind(a, b):
    while True:
        a = input('Sisestage torti nimi:')
        b = int(input('Sisestage torti suurus:'))
        if a == 'šokolaadikook':
            hind = b * b * pi * 0.06
            print('Koogi hind on ', str(hind))
            break
        if a == 'ploomikook':
            hind = b * b * pi * 0.04
            print('Koogi hind on ', str(hind))
            break
        if a == 'Napoleoni_kook':
            hind = b * b * 0.10
            print('Koogi hind on ', str(hind))
            break
        
print(round(str(koogi_hind(a, b)), 2))
