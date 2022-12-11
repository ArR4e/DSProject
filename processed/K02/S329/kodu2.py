print("Tere, kallis kasutaja.")
print("Allpool teil on vaja kirjutada joone pikkus (täisarvuline arv meetrites) ja kõrvutiasetsevate postide maksimaalne kaugus (täisarvuline arv meetrites).")
print("Pärast numbrite sisestamist kuvatakse joone tõmbamiseks vajalike postide minimaalne arv.")

from math import*
P = int(input("Palun kirjutage liini pikkus: "))
L = int(input("Palun kirjutage maksimaalne postidevaheline kaugus: "))

S = ceil(P / L)
D = S + 1
print(D)
