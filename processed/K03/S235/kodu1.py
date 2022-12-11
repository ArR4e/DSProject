palk = float(input("Sisestage aastatulu: "))
if palk <=  6000:
    a = float(palk)
if 6000 < palk <= 14400:
    a = 6000
if 14400 < palk <= 25200:
    a = 6000 - (6000 / 10800 * (palk - 14400))
if palk > 25200:
    a = 0

b = round(a, 2)
print(float(b))