from math import *

l_pikkus = int(input("Sisesta siia sirgjoonelise elektriliini pikkus täisarvuna meetrites: "))
p_vahe = int(input("Sisesta siia kõrvutiasetsevate postide maksimaalkaugus täisarvuna meetrites: "))

if l_pikkus and p_vahe > 0 :
        a = ceil(l_pikkus / p_vahe) + 1
        print("Vaja läheb", a, "posti.")
        
else:
    print("Mõõtmed ei saa olla negatiivsed!")