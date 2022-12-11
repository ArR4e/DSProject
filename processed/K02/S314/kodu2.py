import math

liini_pikkus = int(input("Sisestage liini pikkus: "))
maksimaalkaugus = int(input("Sisestage postide maksimaalkaugus: "))


print("Liini ehitamiseks vajalik postide arv: " + str(math.ceil(liini_pikkus / maksimaalkaugus)+ 1))