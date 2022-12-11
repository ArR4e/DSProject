aastatulu = input("Sisesta aastatulu: ")
tulu = float(aastatulu)

if tulu <= 0:
    print("Maksuvaba tulu on 0 eurot.")
elif tulu <= 6000:
    print("Maksuvaba tulu on ", aastatulu, "eurot.")
elif tulu <= 14400:
    print("Maksuvaba tulu on ", 6000, "eurot.")
elif tulu <= 25200:
    print("Maksuvaba tulu on ", 6000 - 6000 / 10800 * (tulu - 14400))
else:
    print("Maksuvaba tulu on 0 eurot")
