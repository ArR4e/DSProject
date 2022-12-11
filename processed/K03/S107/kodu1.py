aastatulu = float(input("Sisesta aastatulu: "))

if aastatulu <= 6000:
    maksuvaba = aastatulu
    print("Maksuvaba tulu on " + str(maksuvaba) + "€")
if aastatulu > 6000  and aastatulu <= 14400:
    maksuvaba = 6000
    print("Maksuvaba tulu on " + str(maksuvaba) + "€")
if aastatulu > 14400 and aastatulu <= 25200:
    valem = 6000 - 6000 / 10800 * (aastatulu - 14400)
    maksuvaba = valem
    print("Maksuvaba tulu on " + str(round(maksuvaba, 2)) + "€")
if aastatulu > 25200:
    maksuvaba = 0
    print("Maksuvaba tulu on " + str(maksuvaba) + "€")