a = float(input("Sisesta aastatulu: "))

b = 6000 - 6000 / 10800 * (float(a) - 14400)

if a < 6000:
    print("Maksuvabatulu on ", end="")
    print(round(a, 2))
#https://progeopik.cs.ut.ee/02_lihtlaused.html
elif a > 6000 and a < 14400:
    print("Maksuvabatulu on 6000")
elif a > 14400 and a < 25200:
    print("Maksuvabatulu on ", end="")
    print(round(b, 2))
else:
    if a > 25200:
        print("Maksuvabatulu on 0")
