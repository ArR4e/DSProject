aastatulu = float(input("Sisesta oma aastatulu:"))

if aastatulu < 6000 and aastatulu > 0:
    maksuvabatulu = aastatulu
elif aastatulu > 6000 and aastatulu < 14400:
    maksuvabatulu = 6000
elif aastatulu > 14400 and aastatulu < 25200:
    maksuvabatulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
elif aastatulu > 25200:
    maksuvabatulu = 0

print("Sinu maksuvaba tulu on " + str(round(maksuvabatulu, 2)) + ".")

