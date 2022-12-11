import math
liin = round(float(input('Sisestage liini pikkus meetrites: ')))
post = round(float(input('Sisestage kõrvuti asetsevate postide maksimaalne vahemaa: ')))
kogus = (liin / post)
print('Vaja läheb minimaalselt ' + str(math.ceil(kogus) + 1) + ' posti.')
