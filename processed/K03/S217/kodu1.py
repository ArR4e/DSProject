tulu = int(input("Sisesta aastatulu: "))
if tulu <= 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif 14400 < tulu <= 25200:
    mvtulu = 6000 - 6000 / 10800 * (tulu - 14400)
    print("Maksuvaba tulu on ", round(mvtulu, 2), "eurot.")
else:
    print("Maksuvaba tulu on 0 eurot.")

