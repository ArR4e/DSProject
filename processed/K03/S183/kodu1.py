tulu = float(input("Sisesta aastatulu: "))

if tulu < 6000:
    raha = tulu
elif tulu <= 14400:
    raha = 6000
elif tulu <= 25200:
    raha = 6000 - 6000 / 10800 * (tulu - 14400)
else:
    raha = 0


print("Maksuvaba tulu on " + str(round(raha, 2)) + " eurot.")