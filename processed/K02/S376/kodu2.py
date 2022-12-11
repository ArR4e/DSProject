import math

l_pikkus = int(input("Sisesta liini pikkus: "))
p_max_kaugus = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus: "))

p_arv = math.ceil(l_pikkus / p_max_kaugus) + 1

print("Liini ehitamiseks kulub minimaalselt " + str(p_arv) + " posti.")