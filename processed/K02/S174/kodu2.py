from math import *

liinipikkus = int(input("Mis on liini pikkus?" + " "))
#print("Liini pikkus on " + str(liinipikkus) + " meetrit")

maksimaalkaugus = int(input("Mis on maksimaalkaugus?" + " "))
#print("Maksimaalkaugus on " + str(maksimaalkaugus) + " meetrit")

postidearv = ceil(liinipikkus / maksimaalkaugus) + 1
print("Postide arv on: " + str(postidearv))