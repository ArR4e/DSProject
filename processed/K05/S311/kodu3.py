from math import *
x = int(input("Sisesta suurte karpide arv: "))
y = int(input("Sisesta väikeste karpide arv: "))
z = float(input("Sisesta moosi kogus kilogrammides: "))
def moos(x, y, z):
    karpe = 0
    while z/5 >= 1 and x > 0 and (z/5 - x)*5-y <= 0:
        x -= 1
        karpe += 1
        z -= 5
    while z >= 1 and y >= 1:
        y -= 1
        karpe += 1
        z -= 1
    if z == 0:
        return(karpe)
    else:
        return(-1)
moos(x, y, z)