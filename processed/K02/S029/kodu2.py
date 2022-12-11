import math

liini_pikkus = int(input("Mis on pikkus?"))
maksimaalkaugus = int(input("Mis on maksimaalkaugus?"))

postide_arv = (liini_pikkus / maksimaalkaugus) + 1

print(math.ceil(postide_arv))
