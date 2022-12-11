import math

x = round(float(input('Kirjuta liini pikkust täisarvuna meetrites: ')))
y = round(float(input('Kirjuta kõrvutiasetsevate postide maksimaalkaugust täisarvuna meetrites: ')))

a = x/y

print('Liini ehitamiseks on minimaalselt vaja ' + str(math.ceil(a) + 1) + ' posti')