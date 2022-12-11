from math import ceil
liini_pikkus = int(input("Sisestage liini kogupikkus: "))
maksimaal_kaugus = int(input("Sisestage postide maksimaalkaugus: "))


minimaalseid = 0

#kui liin saab pikem olla kui liini on antud siis on ka ainult 2 posti vaja
if maksimaal_kaugus >= liini_pikkus:
    minimaalseid = 2 # 2 sest esimene JA viimane post
else:
    # liidan muutujale minimaalseid 1 sest viimane post peab ka arvesse minema
    minimaalseid = ceil(liini_pikkus / maksimaal_kaugus) + 1


print("Elektriliini ehitamiseks on vaja minimaalselt " + str(minimaalseid) + " posti.")