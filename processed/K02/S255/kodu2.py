from math import *
alguspost = 1
liin_pikkus = float(input("sisesta elektriliini pikkus: "))
kaugus_post = float(input("sisesta kahe posti vaheline kaugus: "))
print("Elektriliini ehitamiseks on vaja " + str(ceil(liin_pikkus / kaugus_post) + (alguspost))  + " elektriposti.")