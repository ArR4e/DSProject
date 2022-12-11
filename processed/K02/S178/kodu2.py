import math

a = int(input('Sisesta liini pikkus (täisarvuna meetrites): '))
b = int(input('Sisesta kõrvutiasetsevate postide maksimaalkaugus teineteisest (täisarvuna meetrites): '))
liiniPikkus= math.ceil(a)
maksimumKaugus= math.floor(b)
postideArv= ((liiniPikkus / maksimumKaugus) + 1.5 )

print(int(postideArv))

