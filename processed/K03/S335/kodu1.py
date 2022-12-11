aastatulu = abs(float(input("Sisestage oma aastatulu: ")))
if aastatulu <= 6000:
    print("Teie maksuvaba tulu on " + str(round(aastatulu, 2)) + " eurot.")
elif 6000 <= aastatulu <= 14400:
    print("Teie maksuvaba tulu on " + str(round(6000.00, 2)) + " eurot.")
elif aastatulu >= 14400 and aastatulu <= 25200:
    print("Teie maksuvaba tulu on " + str(round((6000 - 6000 / 10800 * (aastatulu - 14400)), 2)) + " eurot.")
elif aastatulu > 25200:
    print("Teie maksuvaba tulu on 0 eurot.")