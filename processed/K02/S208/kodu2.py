import math
pikkus = int(input("Sisesta elektriliini kogupikkus: "))
maksimaalkaugus = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus: "))
post = int(math.ceil(pikkus / maksimaalkaugus)) + 1
if post > 1 :
    print("Liini ehitamiseks läheb vaja" , post , "posti.")
else:
    print("Liini ehitamiseks läheb vaja" , post +1 , "posti.")