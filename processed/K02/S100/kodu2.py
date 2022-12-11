pikkus=int(input("Sisestage elektriliini pikkus täisarvuna meetrites: "))
vahe=int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus täisarvuna meetrites: "))

if pikkus%vahe == 0:
    print(pikkus//vahe +1)
else:
    print(pikkus//vahe +2)