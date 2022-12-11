import math
x  = int(input("Sisestage liini pikkus: "))
z = int(input("Sisestage kõrval asetsevate postide maksimaalne kaugus"))
print(math.ceil(x/z)-1+2)