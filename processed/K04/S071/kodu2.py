# Koosta funktsioon nimega summa, mille parameetriteks on kiirused u ja v ning mis tagastab nende kiiruste summa Einsteini erirelatiivsusteooria järgi.
# c = 299792,458 km/s    # u + v / 1 + [(u * v) / c**2]

# Arvuta selle funktsiooni abil nelja samas suunas liikuva keha kiiruste summa, kui kehad liiguvad üksteise suhtes kiirustega u, v, x, y.
# Andmed küsib programm kasutajalt.
# Juhis: Kõigepealt leia kahe esimese kiiruse summa. Siis leia selle ja kolmanda kiiruse summa. Lõpuks leia selle ja neljanda kiiruse summa.

def summa(u,v):
    vastus = (u + v) / (1 + ((u * v) / 89875517873.68175))
    return(vastus)


keha1 = float(input("Esimese keha kiirus vaatleja suhtes on: "))     # 100000
keha2 = float(input("Teise keha kiirus esimese keha suhtes on: "))          # 150000
vastus2 = summa(keha1,keha2)
keha3 = float(input("Kolmanda keha kiirus teise keha suhtes on: "))       # 200000
vastus1 = summa(vastus2,keha3)
keha4 = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))   # 250000
vastus = summa(vastus1,keha4)

print("Kiiruste summa on", vastus,"km/s") # 297993.41836837644 km/s
