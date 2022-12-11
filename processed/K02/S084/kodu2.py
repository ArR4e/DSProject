from math import *

liinipikkus = float(input("Sisestage liini pikkus: "))
postidekaugus = float(input("Sisestage kõrvuti olevate postide kaugus: "))
postid = int(ceil(liinipikkus / postidekaugus) + 1)
print(f"Ehitamiseks on vaja minimaalselt {postid} posti")