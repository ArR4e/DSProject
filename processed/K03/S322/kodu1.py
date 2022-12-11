tulu = float(input("Sisestage aastatulu: "))
maksuvaba = tulu
if tulu > 6000 and tulu <= 14400:
    maksuvaba = 6000.0
elif tulu > 14400 and tulu <= 25200:
    maksuvaba = 6000 - 6000 / 10800 * (tulu - 14400)
elif tulu > 25200:
    maksuvaba = 0.0
print(f"Maksuvaba tulu on {round(maksuvaba, 2)} eurot")