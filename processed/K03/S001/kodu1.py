tulu = float(input("Sisesta aastatulu: "))
maksuvaba = 0

if tulu < 6000:
    maksuvaba = tulu
elif tulu < 14400:
    maksuvaba = 6000
elif tulu < 25200:
    maksuvaba = 6000 - 6000 / 10800 * (tulu - 14400)
else:
    majsuvaba = 0

maksuvaba = round(maksuvaba, 2)
print("Maksuvaba tulu on " + str(maksuvaba) + " eurot.")