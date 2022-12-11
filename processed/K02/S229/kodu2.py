import math
liini_pikkus= int(input("Sisesta liini pikkus meetrites: "))
maxkaugus = int(input("Sisesta kõrval asetsevate postide maksmaalne kaugus meetrites: "))
minposte = math.ceil(liini_pikkus / maxkaugus)

print("Liini ehitamiseks on minimaalselt vaja " + str(minposte)  + " posti.")