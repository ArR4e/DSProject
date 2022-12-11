import math
liin = int(input("Sisestage liini pikkus meetrites: "))
vahe = int(input("Sisestage kõrvuti seisvate postide maksimaalkaugus: "))
postide_arv = liin/vahe +1
print(int(math.ceil(postide_arv)))


