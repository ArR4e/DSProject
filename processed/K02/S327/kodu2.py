import math
liini_pikkus = int(input("Sisestage liini pikkus meetrites: "))
posti_vahe = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus meetrites: "))

poste_vaja = math.ceil(liini_pikkus / posti_vahe + 1)

print(poste_vaja)