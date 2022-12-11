from math import *
liin = int(input("Sisestage liini pikkus meetrites: "))
vahe = int(input("Sisestage postide vaheline maksimaalne kaugus meetrites: "))
if liin < vahe:
    postid = 2
else:
    postid = ceil(liin/vahe + 1)

print("Antud tingimustel liini ehitamiseks on vaja vähemalt", postid, "posti.")