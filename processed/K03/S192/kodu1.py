x = aastatulu = float(input("Sisesta aastatulu: "))
y = maksuvaba_tulu = float(6000)
valem = 6000 - 6000 / 10800 * (aastatulu - 14400)
if x >= 0 and x < 6000:
    print(round(x, 2))
elif x >= 6000 and x < 14400:
    print(round(y, 2))
elif x >= 14400 and x <= 25200:
    print(round(valem, 2))
elif x > 25200:
    print(round(0, 2))
else:
    print("Sisesta positiivne arv")