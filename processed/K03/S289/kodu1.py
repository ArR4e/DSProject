aastatulu = float(input("Palun sisesta aastatulu: "))
x = 6000 - 6000 / 10800 * (aastatulu - 14400)
if aastatulu <= 6000:
    print(aastatulu)
elif 6000 < aastatulu <= 14400:
    print(6000)
elif 14400 < aastatulu <= 25200:
    print(round(x, 2))
else:
    print(0)

