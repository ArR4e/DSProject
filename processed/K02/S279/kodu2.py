from math import *

liini_pikkus = int(input("Sisesta elektriliini pikkus: "))
max_kaugus = int(input("Sisesta postide maksimaalkaugus: "))

postid_kokku = ceil(liini_pikkus/max_kaugus) + 1

print("Liini ehitamiseks on minimaalselt vaja", postid_kokku, "posti.")