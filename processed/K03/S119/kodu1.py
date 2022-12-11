aastatulu = float(input("Palun sisesta oma aastatulu: "))
a = (6000 - (6000 / 10800) * (int(aastatulu) - 14400))
if aastatulu <= 6000:
    print("Maksuvabatulu on " + (str(round (aastatulu, 2))) + " eurot")
if aastatulu in range(6000, 14400):
    print("Maksuvabatulu on " + str(6000) + " eurot")
if aastatulu in range(14400, 25200):
    print("Maksuvabatulu on " + str(round( a, 2)) + " eurot")
if aastatulu > 25200:
    print("Maksuvabatulu on " + str(0) + " eurot")