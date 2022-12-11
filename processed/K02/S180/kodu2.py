from math import *

x = int(input("Mis on liini pikkus meetrites?: "))
y = int(input("Kõrvuti astetsevate postide maksimaalkaugus?: "))

z = ceil(x/y)
if z==float():
    print('Minimaalselt on vaja' + ' ' + str(z + 1) + ' ' + 'posti.')
else:
    print('Minimaalselt on vaja' + ' ' + str(z + 1) + ' ' + 'posti.')