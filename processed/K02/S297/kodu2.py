import math

liini_pikkus = int(input('Sisestage liini pikkus meetrites:'))
postide_vahe = int(input('Sisestage postide vahe meetrites:'))

postide_arv = math.ceil(liini_pikkus / postide_vahe) + 1

print('Liini rajamiseks läheb vaja ' + str(postide_arv) + ' posti.')