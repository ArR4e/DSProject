# 2. Einsteini erirelatiivsusteooria
# Koosta funktsioon nimega summa, mille parameetriteks on kiirused u ja v ning mis tagastab nende kiiruste summa Einsteini erirelatiivsusteooria järgi.
def summa(u, v):
    c = 299792.458 # km/s
    summa1 = (u +v)/(1 + ((u*v)/c**2))
    return summa1

# Arvuta selle funktsiooni abil nelja samas suunas liikuva keha kiiruste summa, kui kehad liiguvad üksteise suhtes kiirustega u, v, x, y.
# Andmed küsib programm kasutajalt.

u = float(input("Esimese keha kiirus: "))
v = float(input("Teise keha kiirus: "))
x = float(input("Kolmanda keha kiirus: "))
y = float(input("Neljanda keha kiirus: "))

print(summa(summa(summa(u, v), x), y))