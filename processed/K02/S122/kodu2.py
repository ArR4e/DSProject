import math

pikkus = float(input("Liini pikkus meetrites: "))
kaugus = float(input("Postide maksimaalkaugus meetrites: "))
postide_arv = pikkus / kaugus + 1
postide_arv_tais = math.ceil(postide_arv)
print("Liini ehitamiseks on minimaalselt vaja " + str(postide_arv_tais) + " posti.")