pikkus = int(input("Sisesta elektriliini kogupikkus täisarvuna meetrites: "))
vahe = int(input("Sisesta kõrvutiasuvate postide maksimaalkaugus täisarvuna meetrites: "))
print("Elektriliini ehitamiseks on vaja minimaalselt ", int(pikkus/vahe+1), "elektriposti.")