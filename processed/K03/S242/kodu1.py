aastatulu = float(input("Sisesta oma aastatulu:"))
if 0 < aastatulu <= 6000:
    aastatulu = round(aastatulu, 2)
    print("Sinu maksuvaba tulu on", aastatulu)
elif 6000 < aastatulu <= 14400:
    print("Sinu maksuvaba tulu on 6000 eurot.")
elif 14400 < aastatulu <= 25200:
    maksuvaba_tulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
    maksuvaba_tulu = round(maksuvaba_tulu, 2)
    print("Sinu maksuvaba tulu on", maksuvaba_tulu)
elif aastatulu > 25200:
    print("Sinu maksuvaba tulu on 0 eurot.")
else:
    print("Sisesta palun positiivne arv")
