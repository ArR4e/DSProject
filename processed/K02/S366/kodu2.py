import math

liinipikkus = int(input("Sisestage liini pikkus meetrites: "))
kaugus = int(input("Sisestage kõrvutiasetsevate poste maksimaalkaugus meetrites: "))


minvaja = 1 + (liinipikkus/kaugus)
print(math.ceil(minvaja))



