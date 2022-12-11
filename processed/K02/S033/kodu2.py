pikkus = int(input("Sisesta elektriliini pikkus meetrites: "))
#100
max_vahe = int(input("Sisesta postide vaheline maksimaalne kaugus meetrites: "))
#25

import math

postide_arv = pikkus / max_vahe + 1
postide_arv2 = math.ceil(postide_arv)

if pikkus < max_vahe:
    print("Liini ehitamiseks on minimaalselt vaja 2 posti.")
else:
    print("Liini ehitamiseks on minimaalselt vaja " + str(postide_arv2) + " posti.")