import math

liinipikkus = int(input("Sisesta liini pikkus: "))
vahekaugus = int(input("Sisesta postide vahekaugus: "))
postide_arv = math.ceil(liinipikkus/vahekaugus+1)
print("Minimaalne postide arv liini ehitamiseks on: " + str(postide_arv))