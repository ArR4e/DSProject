import math

liin = int(input('Sisestage, palun, liini pikkus: '))
post = int(input('Sisestage, palun, maksimaalne postidevaheline kaugus: '))

if post > liin * 0.5:
    print(int(liin / math .floor (post) + 2))
else:
    print(int(liin / math .floor (post) + 1))