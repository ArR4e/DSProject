at = float(input("Sisesta aastatulu: "))
if at <= 6000:
    mvt = at
elif at >6000 and at <= 14400:
    mvt = 6000
elif at > 14400 and at <= 25200:
    mvt = 6000 - 6000/10800*(at-14400)
elif at > 25200:
    mvt = 0
print(round(mvt, 2))