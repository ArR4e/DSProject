tulu = float(input("Sisestage aastatulu: "))

if tulu <= 6000:
    maksuvaba = tulu
elif tulu <= 14400:
    maksuvaba = 6000
elif tulu <= 25000:
    maksuvaba = 6000 - (6000/10800)*(tulu - 14400)
else:
    maksuvaba = 0

print("Maksuvaba tulu on {maksuvaba} eurot.".format(maksuvaba = round(maksuvaba, 2)))