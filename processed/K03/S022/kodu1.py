tulu = -1
while tulu < 0:
    tulu = float(input("Sisesta oma aastatulu: "))

if tulu < 6000:
    maksuvaba = tulu
    print("Maksuvaba tulu on", maksuvaba, "eurot.")
if tulu < 14400:
    maksuvaba = 6000
    print("Maksuvaba tulu on", maksuvaba, "eurot.")
elif tulu < 25200:
    maksuvaba = 6000 - 6000/10800 * (tulu - 14400)
    maksuvaba = round(maksuvaba, 2)
    print("Maksuvaba tulu on", maksuvaba, "eurot.")
else:
    maksuvaba = 6000
    maksuvaba = maksuvaba - 6000
    print("Maksuvaba tulu on", maksuvaba, "eurot.")