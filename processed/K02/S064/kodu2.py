from math import *
a = int(input("Sisestage liini pikkus meetrites: "))
b = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus meetrites: "))

postide_arv = ceil(a/b+1)
print(int(postide_arv))