from math import *
liini_pikkus=int(input("Sisestage elektriliini pikkus meetrites: "))
postidevaheline_maxkaugus=int(input("Sisestage postidevaheline maksimaalne kaugus:_meetrites: "))
postide_arv = ceil(liini_pikkus/postidevaheline_maxkaugus) + 1
print("Liini ehitamiseks on vaja minimaalselt " + str(postide_arv) + " posti.")