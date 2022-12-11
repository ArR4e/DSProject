aastatulu = float(input("Sisesta aastatulu: "))

def tulu(a):
    print("Maksuvaba tulu on", a, "eurot.")

if aastatulu < 6000 and aastatulu > 0:
    tulu(aastatulu)
elif aastatulu < 14400:
    tulu(6000)
elif aastatulu < 25200:
    ümardatudtulu = round(6000 - 6000 / 10800 * (aastatulu - 14400), 2)
    tulu(ümardatudtulu)
else:
    tulu(0)