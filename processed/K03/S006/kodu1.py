aastatulu = float(input("Sisesta siia aastatulu eurodes: "))
lause = "Aastane maksuvaba tulu eurodes on: "
if aastatulu <= 0:
    print("Aastatulu saab olla vaid positiivne!")
else:
    if aastatulu <= 6000:
        print(lause + str(aastatulu))
    elif aastatulu <= 14400:
        print(lause + "6000")
    elif aastatulu <= 25200:
        aastatulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
        print(lause + str(round(aastatulu, 2)))
    else:
        print(lause + "0")