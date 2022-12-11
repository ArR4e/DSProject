aastatulu = float(input("Sisestage aastatulu: "))
if aastatulu <= 6000:
    print("Teie maksuvaba tulu on :" + str(aastatulu))
elif 6000 < aastatulu <= 14400:
    print("Teie maksuvaba tulu on : 6000")
elif 14400 < aastatulu <= 25200:
    maksuvabatulu = round((6000 - 6000 / 10800 * (aastatulu - 14400)),2)
    print("Teie maksuvaba tulu on :" + str(maksuvabatulu))
elif aastatulu > 25200:
    print("Teie maksuvaba tulu on: 0")