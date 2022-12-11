from math import *

a = 200
print("Kõrvutiasetsevate postide suurim lubatud kaugus on", a, "meetrit")
l = int(input("Sisestage soovitud elektriliini pikkus meetrites: "))
s = int(input("Sisestage kõrvutiasetsevate postide kaugus meetrites: "))
n = int(l/s) + 1
if s <= a:
    print("Liini ehitamiseks kulub vähemalt",n,"posti")
else:
    print("Postide vaheline kaugus ületab etteantud suurust, proovi uuesti")
if s > l:
    print("Võimatu, proovi uuesti")
