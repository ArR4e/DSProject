#KN
from math import*

pikkus = float(input("Sisestage liini pikkus meetrites: "))
maksimaalne = float(input("Sisestage postide maksimaalkaugus meetrites: "))
postid = ceil(pikkus/maksimaalne)+1
print("Liini ehitamiseks on vaja minimaalselt " + str(postid) + " posti.")

