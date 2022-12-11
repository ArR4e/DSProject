import math

pikkus= input("Sisesta liini pikkus meetrites: ")
a=int(pikkus)

kaugus=input("Sisesta postide maksimaalne kaugus meetrites: ")
b=int(kaugus)

x = ((a/b)+1)

vastus=math.ceil(x)

print("Liini ehitamiseks on vaja minimaalselt " + str(vastus) + " posti.")