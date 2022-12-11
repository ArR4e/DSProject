from math import *
pikkus = int(input('Mis on liini pikkus meetrites?'))
vahe = int(input('Mis on kõrvuti asetsevate postide maksimaalne kaugus meetrites?'))

min_poste = int(ceil(pikkus/vahe) + 1)

print('Minimaalselt on vaja', min_poste, 'posti')