from math import *

pikkus = int(input("Sisesta liini pikkus meetrites: "))
maxkaugus = int(input("Sisesta postide maksimaalkaugus meeetrites: "))

postidearv = ceil(1+(pikkus/maxkaugus))
postidearv = int(postidearv)

if maxkaugus > pikkus:
    print(postidearv + 1)



print(int(postidearv))