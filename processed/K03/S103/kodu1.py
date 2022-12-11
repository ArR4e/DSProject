aastatulu = float(input("Sisesta aastatulu: "))

if aastatulu < 0:
    raise Exception("Sisesta positiivne number.")
elif aastatulu <= 6000:
    print("Maksuvaba tulu on", aastatulu, "eurot.")
elif aastatulu >= 6000 and aastatulu <= 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif aastatulu >= 14400 and aastatulu <= 25200:
    maksuvaba_tulu = 6000-6000 / 10800 * (aastatulu - 14400)
    print("Maksuvaba tulu on", round(maksuvaba_tulu, 2), "eurot.")
else:
    print("Maksuvaba tulu on 0 eurot.")