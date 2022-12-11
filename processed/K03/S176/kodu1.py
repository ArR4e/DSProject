aastatulu = float(input("Sisesta aastatulu: "))
if 0 <= aastatulu <= 6000:
    print("Maksuvaba tulu on ", aastatulu, "eurot")
elif 6000 < aastatulu <= 14400:
    print("Maksuvaba tulu on 6000 eurot")
elif 14400 < aastatulu <= 25200:
    maksuvaba = 6000 - 6000 / 10800 * (aastatulu - 14400)
    print("Maksuvaba tulu on ", round(maksuvaba, 2), "eurot")
elif 25200 < aastatulu:
    print("Maksuvaba tulu on 0 eurot")
else:
    print("Maksuvaba tulu ei saa arvutada")