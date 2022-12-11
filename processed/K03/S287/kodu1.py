tulu = float(input("Sisestage aastatulu: "))

if tulu < 6000:
    print(f"Maksuvaba tulu on {round(tulu, 2)} eurot")
elif tulu < 14400:
    print(f"Maksuvaba tulu on 6000 eurot")
elif tulu < 25200:
    mtulu1 = round(6000 - 6000 / 10800 * (tulu - 14400), 2)
    print(f"Maksuvaba tulu on {mtulu1} eurot")
elif tulu > 25200:
    print("Maksuvaba tulu on 0 eurot") 