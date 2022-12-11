#kodu2
pikkus=int(input("Sisesta liini pikkus meetrites: "))
kaugus=int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus meetrites: "))
if pikkus==kaugus:
    poste=2
else:
    if pikkus==2*kaugus:
        poste=3
    else:
        poste=pikkus/kaugus+2
print("Liini ehitamiseks on vaja vähemalt ", int(poste), " posti.")