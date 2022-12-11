import math
pikkus = int(input("Sisestage liini pikkus: "))
kaugus = int(input("Sisetage maksimaalne kaugus: "))

print("Liini ehitamiseks on minimaalselt vaja " + str(math.ceil(pikkus/kaugus)+1) + " posti")
