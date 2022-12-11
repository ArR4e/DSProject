# Elektriliin
from math import ceil

max_kaugus = int(input("Sisesta elektriliini maksimaalne kaugus: "))
postide_vahe = int(input("Sisesta postide maksimaalne vahekaugus: "))

if max_kaugus > postide_vahe:
    postid = ceil(max_kaugus / postide_vahe) + 1
else:
    postid = 2


print("Elektriliini ehitamiseks kulub: " + str(postid) + " posti")