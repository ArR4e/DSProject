aastatulu = float(input("Sisestage aastatulu: "))
if aastatulu < 6000:
    maksuvaba_tulu = aastatulu
    print("Maksuvaba tulu on", round(maksuvaba_tulu, 2), "eurot.")
else:
    if aastatulu < 14400:
        maksuvaba_tulu = 6000
        print("Maksuvaba tulu on", maksuvaba_tulu, "eurot.")
    elif aastatulu < 25200:
        maksuvaba_tulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
        print("Maksuvaba tulu on", round(maksuvaba_tulu, 2), "eurot.")
    else:
        maksuvaba_tulu = 0
        print("Maksuvaba tulu on", maksuvaba_tulu, "eurot.")