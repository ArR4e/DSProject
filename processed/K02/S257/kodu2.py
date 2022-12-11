
from math import *

l_pikkus = int(input("Sisesta liini pikkus täisarvudes: "))
max_kaugus = int(input("Sisesta kahe posti vaheline maksimaalne kaugus täisarvudes: "))

postide_arv = ceil(l_pikkus / max_kaugus) + 1

print("Vaja läheb ", postide_arv, " posti.")