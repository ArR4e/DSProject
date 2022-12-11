nöör = float(input("Sisesta elektriliini pikkus: "))
vahe = float(input("Sisesta kõrvuti asetsevate postide maksimaalne kaugus: "))
if nöör/vahe < 1:
    arv = 2
else:
    if nöör%vahe == 0:
        arv = int(nöör//vahe + 1)
    else:
        arv = int(nöör//vahe + 2)
print ("Liini ehitamiseks on vaja", arv , "posti.")