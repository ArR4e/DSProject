from math import *

liinipikkus = int(input("Sisesta liini pikkus meetrites: "))
postikaugusmax = int(input("Sisesta postidevaheline maksimaalne kaugus meetrites: "))

minimaalarv = ceil((liinipikkus/postikaugusmax))+1

print(minimaalarv)