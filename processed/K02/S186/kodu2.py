a=float(input("Sisesta liini pikkus täisarvuna meetrites: "))
b=float(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus täisarvuna meetrites: "))
import math
summa=math.ceil(a/b+1)
print("Liini ehitamiseks on minimaalselt vaja " + str(summa)+" posti.")