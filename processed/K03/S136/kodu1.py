aastatulu = int(input("Sisesta oma aastatulu: "))
if aastatulu < 14000:
    print("6000")
else:
    if aastatulu >= 14000 and aastatulu <= 25200:
        print(6000 - 6000 / 10800 * (aastatulu - 14400))
    else:
        if aastatulu > 25200:
            print("0")