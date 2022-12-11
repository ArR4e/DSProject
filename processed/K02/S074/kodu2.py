from math import ceil
#Kusib kasutajalt liini pikkust
pikkus = int(input("Sisesta liini pikkus: "))
#Kusib kasutajalt korvutiasetsevate postide maksimaalkauguse
kaugus = int (input("Sisesta postide maksimaalkaugus: "))
#Arvutab mitu posti on liini ehitamiseks vaja
kogus = ceil(pikkus/kaugus) +1
#Valjastab postide arvu mida vaja laheb
print(kogus)