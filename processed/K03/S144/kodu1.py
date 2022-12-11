tulu = float(input("Sisesta maksuvaba tulu: "))

if tulu <= 6000:
    print(f"Maksuvaba tulu on {round(tulu, 2)} eurot.")

if 6000 < tulu <= 14400:
    print("Maksuvaba tulu on 6000 eurot.")

if 14400 < tulu <= 25200:
    maksuvabatulu = 6000 - 6000 / 10800 * (tulu - 14400)
    print(f"Maksuvaba tulu on {round(maksuvabatulu, 2)} eurot.")
if tulu > 25200:
    print("Maksuvaba tulu on 0 eurot.")