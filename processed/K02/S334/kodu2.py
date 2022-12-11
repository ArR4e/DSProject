from math import ceil
lp = int(input("Liini pikkus: "))
pk = int(input("Postide kaugus: ")) #vahe liht
print("Minimaalselt on vaja: ", ceil(lp / pk + 1))
