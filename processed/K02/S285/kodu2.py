pikkus = int (input ("Sisestage liini pikkus: "))
kaugus = int (input ("Sisestage kahe liini vaheline kaugus: "))

if pikkus == 2 and kaugus == 1:
    print (3)

elif pikkus == kaugus:
    print (2)

elif pikkus / kaugus == kaugus:
    print (3)

else:
    print (int (pikkus / kaugus + 2))