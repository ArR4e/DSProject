a = float(input("Sisestage oma aastatulu: "))

if a < 6000:
    print("Maksuvaba tulu on: ", a)
elif a >= 6000 and a < 14400:
    print("Maksuvaba tulu on 6000")
elif a >= 14400 and a < 25200:
    mvaba = 6000 - (6000 / 10800 * (a - 14400))
    vabatulu = round(mvaba, 2)
    print("Maksuvaba tulu on ", vabatulu)
else:
    print("Maksuvaba tulu on 0")
    