import math
def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1) * n
def autohind(väärtus,aasta):
    fact(aasta)
    if aasta == 0:
        return väärtus
    while aasta > 0:
        juurdehindlusprotsent = 20
        uus_hind = väärtus * (1 -(juurdehindlusprotsent/100))
        väärtus = uus_hind
        aasta -= 1
    return väärtus
print(float(round(autohind(8000,5),2)))
