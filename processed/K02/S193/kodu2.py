from math import*
Pikkus = int(input("Palun sisestage liini pikkus(täisarvuna meetrites): "))
Kaugus = int(input("Palun sisestage kõrvutiasetsevate postide maksimaalkaugus(täisarvuna meetrites): "))

S = ceil(Pikkus / Kaugus)
D = S + 1
print(D)