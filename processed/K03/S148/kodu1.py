aastatulu = float(input("Sisesta aastatulu: "))

while aastatulu < 0:
    aastatulu = float(input("Sisesta aastatulu: "))

if 0 < aastatulu <= 6000:
    maksuvaba = aastatulu
elif 6000 < aastatulu <= 14400:
    maksuvaba = 6000
elif 14400 < aastatulu <= 25200:
    maksuvaba = 6000 - 6000 / 10800 * (aastatulu - 14400)
else:
    maksuvaba = 0

maksuvaba_2 = round(maksuvaba, 2)
print("Maksuvaba tulu on", maksuvaba_2, "eurot.")