pikkus = int(input("Palun sisesta liini pikkus täisarvuna meetrites: "))

kaugus = int(input("Palun sisesta postide maksimaalne kaugus täisarvuna meetrites: "))

from math import*

postide_arv = pikkus/kaugus

print("Liini ehitamiseks läheb minimaalselt vaja " + str(ceil(postide_arv + 1)) + " posti!")