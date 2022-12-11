import math
liini_pikkus = int(input("Sisesta elektriliini pikkus: "))
max_posti_kaugus = int(input("Sisesta maksimaalne postidevaheline kaugus: "))



if liini_pikkus < max_posti_kaugus:
    postide_arv = 2
    print("Liini ehitamiseks vajalik postide arv on: ", postide_arv)
else:
    x = liini_pikkus / max_posti_kaugus + 1
    postide_arv = math.ceil(x)
    print("Liini ehitamiseks vajalik postide arv on: ", postide_arv)