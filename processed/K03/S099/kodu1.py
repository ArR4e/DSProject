tulu = float(input("Sisesta aastatulu (€): "))

if tulu <= 6000:
    maksuvaba = tulu
elif tulu <= 14400:
    maksuvaba = 6000
elif tulu <= 25200:
    maksuvaba = 6000 - 6000 / 10800 * (tulu - 14400)
elif tulu > 25200:
    maksuvaba = 0
else:
    print("Sisestuse viga!")
print("Maksuvaba tulu on", round(maksuvaba, 2))