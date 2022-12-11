from math import *

liinipikkus = int(input("Kirjuta liini pikkus meetrites: "))
max_kaugus = int(input("Sisesta kõrvutiasetsevate postide max kaugus üksteisest: "))

vastus = ceil(1 + liinipikkus / max_kaugus)

print(vastus)

