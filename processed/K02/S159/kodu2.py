import math

maksimum = float(input('Sisesta elektriliini kogupikkus: '))
samm = float(input('Sisesta elektripostide maksimaalne kaugus üksteisest: '))

kogupostid = maksimum / samm

tarvis = math.ceil(kogupostid) + 1

if tarvis == 1:
    print('Sul on vaja 2 posti!')
if tarvis > 1:    
    print('Sul on vaja ' + str(tarvis) + ' posti!')