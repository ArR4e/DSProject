aastatulu = abs(float(input("Sisesta aastatulu: ")))
if aastatulu < 6000:
    maksuvaba = aastatulu
elif aastatulu < 14400:
    maksuvaba = 6000
elif aastatulu < 25200:
    maksuvaba = 6000 - 6000 / 10800 * (aastatulu - 14400)
else:
    maksuvaba = 0
maksuvaba = round(maksuvaba, 2)
print("Maksuvaba tulu on", maksuvaba, "eurot")
