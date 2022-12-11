import math

pikkus = int(input("Sisesta liini pikkus meetrites: "))
kaugus = int(input("Sisesta kõrvutiseisvate postide maksimaalkaugus meetrites: "))

arv = pikkus / kaugus
arv_ümardatud = int(math.ceil(arv))
postide_arv = arv_ümardatud +1


print("Liini ehitamiseks on minimaalselt vaja " + str(postide_arv) + " " + "posti.")
