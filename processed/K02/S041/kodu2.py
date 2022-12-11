import math

liini_pikkus = int(input("Mis on pikkus?"))
maksimaalkaugus = int(input("Mis on maksimaalkaugus?"))

postidearv = (liini_pikkus / maksimaalkaugus) + 1

print(math.ceil(postidearv))