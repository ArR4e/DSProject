aastatulu = float(input("Sisesta aastatulu: "))

if aastatulu >= 0:
    if aastatulu <= 6000:
        maksuvaba_tulu = aastatulu
        print("Maksuvaba tulu on", round(maksuvaba_tulu, 2), "eurot.")
    if 6000 < aastatulu <= 14400:
        maksuvaba_tulu = 6000
        print("Maksuvaba tulu on", round(maksuvaba_tulu, 2), "eurot.")
    if 14400 < aastatulu <= 25200:
        maksuvaba_tulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
        print("Maksuvaba tulu on", round(maksuvaba_tulu, 2), "eurot.")
    if aastatulu > 25200:
        maksuvaba_tulu = 0
        print("Maksuvaba tulu on", round(maksuvaba_tulu, 2), "eurot.")

else:
    print("Tulu peab olema positiivne!")