import math
liini_pikkus = int(input("Sisestage elektriliini pikkus (täisarvuna meetrites): "))
postide_kaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalne vahekaugus (täisarvuna meetrites): "))
print("Elektriliini ehitamiseks on minimaalselt tarvis " + str(math.ceil(liini_pikkus/postide_kaugus)) + " posti.")