aastatulu = input("Sisestage aastatulu: ")
aastatulu = float(aastatulu)

maksuvabatulu = round(6000 - 6000 / 10800 * (aastatulu - 14400), 2)


print("maksuvabatulu", maksuvabatulu)