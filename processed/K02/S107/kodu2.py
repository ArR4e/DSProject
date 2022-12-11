import math
liini_pikkus = int(input("Sisesta elektriliini pikkus: "))
postide_vahe = int(input("Sisesta postide vaheline kaugus: "))

print("Liini ehitamiseks kulub " + str(math.ceil(liini_pikkus / postide_vahe + 1)), "posti")
    
