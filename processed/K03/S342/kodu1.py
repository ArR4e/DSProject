tulu = float(input("Sisesta aastatulu: "))
while tulu < 0:
    tulu = float(input("Sisesta positiivne aastatulu: "))
if tulu <= 6000:
    maksuvaba = tulu
elif 6000 < tulu <= 14400:
    maksuvaba = 6000
elif 14400 < tulu <= 25200:
    maksuvaba = 6000 - 6000 / 10800 * (tulu - 14400)
else:
    maksuvaba = 0
print("Maksuvaba tulu on " + str(round(maksuvaba, 2)) + " eurot.")