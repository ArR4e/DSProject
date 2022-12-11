from math import *

liini_pikkus = int(input("Sisesta elektriliinide pikkus: "))
maksimaalkaugus = int(input("Sisesta postide maksimaalkaugus: "))

max_postid = liini_pikkus // maksimaalkaugus

if liini_pikkus <= maksimaalkaugus:
    summa = 2
elif liini_pikkus / maksimaalkaugus == 2:
    summa = max_postid + 1
else:
    summa = max_postid + 2
    
print(summa)