aastatulu = int(input("Sisesta oma aastatulu: "))

if aastatulu <= 6000:
    print("Maksuvaba tulu on ", aastatulu, "eurot aastas")
elif aastatulu <= 14400:
    print("Maksuvaba tulu on 6000 eurot aastas")
elif aastatulu <= 25200:
    print("Maksuvaba tulu on ", round(6000 - 6000 / 10800 * (aastatulu - 14400), 2), "eurot aastas")
else:
    print("Maksuvaba tulu on 0 eurot aastas")

